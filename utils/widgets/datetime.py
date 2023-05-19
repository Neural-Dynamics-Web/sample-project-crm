# region				-----External Imports-----
import django
# endregion


class CustomSplitDateTime(
        django.contrib.admin.widgets.AdminSplitDateTime
    ):
    
    def __init__(self,
            format="%H:%M",
            attrs=None
        ) -> None:
        widgets = [
            django.contrib.admin.widgets.AdminDateWidget,
            django.contrib.admin.widgets.AdminTimeWidget(
                format=format,
                attrs=attrs
            )
        ]
        django.forms.MultiWidget.__init__(self, widgets, attrs)

