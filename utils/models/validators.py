# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
# endregion


def positive_validator(
        value: typing.Union[int, float]
    ) -> typing.Union[int, float]:
    if value <= 0:
        raise django.core.exceptions.ValidationError(
            _("Value can't be less or equals 0")
        )

    return value


def audio_file_validator(
        value: typing.AnyStr
    ) -> typing.Any:
    if ".mp3" not in value.path:
        raise django.core.exceptions.ValidationError(
            _("Only .mp3 format is allowed")
        )

    return value