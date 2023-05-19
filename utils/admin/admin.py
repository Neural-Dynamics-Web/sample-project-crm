# region				-----External Imports-----
import django
import typing
# endregion


class ReadonlyFieldsOnCRUD(django.contrib.admin.ModelAdmin):
    read_only_fields_on_update = []


    def get_readonly_fields(self,
            request: django.http.HttpRequest,
            obj: django.db.models.Model = None
        ) -> typing.List[str]:
        if obj:
            result_fields = tuple(self.read_only_fields_on_update)\
                          + tuple(self.readonly_fields)
            return result_fields
        return self.readonly_fields
