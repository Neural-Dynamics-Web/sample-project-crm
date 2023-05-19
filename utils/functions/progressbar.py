# region				-----External Imports-----
import django
import typing
import random
# endregion

def progress_bar(
        completion: int,
        color: str
    )\
    -> typing.AnyStr:
    return django.utils.html.format_html(
        """
        <div class="progress">
                <div class="progress-bar" style="width:{completion}%; background:{color};">
                    <div class="progress-value">{completion}%</div>
                </div>
            </div>
        """,
        completion=completion,
        color=color
    )