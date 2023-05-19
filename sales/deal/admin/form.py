# region				-----External Imports-----
import django
# endregion

# region				-----Internal Imports-----
from .. import models as local_models
# endregion


class DealForm(django.forms.ModelForm):
    # region			   -----Validators-----
    def clean_project(self):
        project = self.cleaned_data.get("project")
        status = self.cleaned_data.get("status")

        if status == "win" and not project:
            raise django.core.exceptions.ValidationError(
                "Project can't be empty if the deal was won"
            )
        
        return project


    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        status = self.cleaned_data.get("status")

        if status == "win" and not amount:
            raise django.core.exceptions.ValidationError(
                "Amount can't be empty if the deal was won"
            )
        
        return amount
    # endregion


    class Meta(object):
        model = local_models.Deal
        fields = "__all__"