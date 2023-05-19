# region				-----External Imports-----
from django.conf import settings
import celery
import logging
import openai
import utils
import os
# endregion

# region				-----Internal Imports-----
from .. import models
# endregion

# region		      -----Supporting Variables-----
logger = logging.getLogger(__name__)
# endregion


@celery.shared_task(name="process_meeting_note")
def process_meeting_note(
        meeting_note_id: str
    ) -> None:
    meeting_note = models.meeting_notes.MeetingNote\
        .objects.get(id=meeting_note_id)
    
    try:        
        meeting_note.status = "processing_audio"
        meeting_note.save()
        
        openai.api_key = settings.OPEN_AI_KEY

        chunks = utils.functions.audio_to_chunks\
            .file_to_chunks(
                file_path=meeting_note.audio.path,
                size_seconds=1200
            )
        
        transcription = ""
        for chunk in chunks:
            transcript = openai.Audio.transcribe(
                file=open(chunk, "rb"),
                model="whisper-1"
            )

            transcription += transcript["text"]

            os.remove(chunk)

        meeting_note.status = "processing_transcript"
        meeting_note.transcript = transcription
        meeting_note.save()

        chunks = utils.functions.audio_to_chunks\
            .divide_text_into_chunks(
                text=transcription,
                chunk_size=1000
            )

        summary = ""
        for chunk in chunks:
            prompt = meeting_note.prompt.format(
                text=chunk
            )

            response = openai.Completion.create(
                engine="text-davinci-003",
                max_tokens=1500,
                prompt=prompt,
                temperature=0,
                stop=None,
                n=1
            )

            if response["choices"][0]["finish_reason"] == "error":
                meeting_note.text = response["choices"][0]["finish_reason"]
                meeting_note.status = "error"
                meeting_note.save()
                break
            else:
                summary += response["choices"][0]["text"]
        else:
            meeting_note.status = "processed"
            meeting_note.text = summary
            meeting_note.save()
    except Exception as error:
        meeting_note.text = str(error)
        meeting_note.status = "error"
        meeting_note.save()