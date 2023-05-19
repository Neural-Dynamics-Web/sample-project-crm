# region				-----External Imports-----
from django.utils.translation import gettext_lazy as _
import admin_auto_filters
# endregion


class ProjectFilter(
        admin_auto_filters.filters.AutocompleteFilter
    ):
    is_placeholder_title = True
    field_name = "project"
    title = _("Project")


class FeatureFilter(
        admin_auto_filters.filters.AutocompleteFilter
    ):
    is_placeholder_title = True
    field_name = "feature"
    title = _("Feature")


class StageFilter(
        admin_auto_filters.filters.AutocompleteFilter
    ):
    is_placeholder_title = True
    field_name = "stage"
    title = _("Stage")


class TaskFilter(
        admin_auto_filters.filters.AutocompleteFilter
    ):
    is_placeholder_title = True
    field_name = "task"
    title = _("Task")