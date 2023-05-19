# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import django
import typing
import utils
# endregion


class Completion(django.contrib.admin.ModelAdmin):
    @django.contrib.admin.display(
        description=_("Development Completion"),
        ordering="completion_development"
    )
    def development_progress_bar(self,
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return utils.functions.progressbar.progress_bar(
            completion=instance.development_completion,
            color="#85B8FC"
        )
    
    
    @django.contrib.admin.display(
        description=_("Delivery Completion"),
        ordering="completion_delivery"
    )
    def delivery_progress_bar(self,
            instance: django.db.models.Model
        ) -> typing.AnyStr:
        return utils.functions.progressbar.progress_bar(
            completion=instance.delivery_completion,
            color="#45CB66"
        )