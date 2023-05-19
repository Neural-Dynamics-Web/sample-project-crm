# region				-----External Imports-----
import pydub
import typing
import time
# endregion


def file_to_chunks(
        file_path: typing.AnyStr,
        size_seconds: int
    ) -> typing.List[str]:
    sound_track = pydub.AudioSegment.from_mp3(file_path)
    duration_seconds = sound_track.duration_seconds

    chunks = int(duration_seconds / size_seconds)\
           + 1
    
    size_milliseconds = size_seconds * 1000
    
    chunk_files = []

    for index in range(chunks):
        name = f"{index}_{int(time.time())}.mp3"
        end = (index + 1) * size_milliseconds
        start = index * size_milliseconds

        chunk = sound_track[start:end]

        chunk_files.append(name)
        chunk.export(name)
    
    return chunk_files


def divide_text_into_chunks(
        text: typing.AnyStr,
        chunk_size: int
    ):
    chunks = []
    current_chunk = ""
    for word in text.split():
        if len(current_chunk) + len(word) <= chunk_size:
            current_chunk += " " + word
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks