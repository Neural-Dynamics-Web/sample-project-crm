# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion


class Completion(django.contrib.admin.ModelAdmin):
    @django.contrib.admin.display(
        description=_("Completion"),
        ordering="completion"
    )
    def progress_bar(self,
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return utils.functions.progressbar.progress_bar(
            completion=instance.completion,
            color="#45CB66"
        )