# region				-----External Imports-----
import django
import typing
# endregion


def admin_changelist_url(instance: django.db.models.Model)\
    -> typing.AnyStr:
    model_name = instance.__name__.lower()
    app_label = instance._meta.app_label

    return django.urls.reverse(
        viewname=f"admin:{app_label}_{model_name}_changelist"
    )


def admin_change_form(instance: django.db.models.Model)\
    -> typing.AnyStr:
    model_name = instance._meta.model.__name__.lower()
    app_label = instance._meta.app_label

    return django.urls.reverse(
        viewname=f"admin:{app_label}_{model_name}_change",
        args=[instance.id]
    )