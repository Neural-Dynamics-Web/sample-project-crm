# region				-----External Imports-----
import django
import typing
import utils
# endregion


def to_related_objects(
        short_description: typing.AnyStr,
        attribute: typing.AnyStr,
        empty_value: str = None
    ) -> typing.Callable:
    
    def wrapper_of_wrapper(function: typing.Callable)\
        -> typing.Callable:

        def default_wrapper(self, 
                instance: django.db.models.Model
            ) -> typing.Any:
            related_object = getattr(instance, attribute, None)
            if not related_object:
                return empty_value
            
            link = utils.functions.change_form.admin_changelist_url(
                instance=related_object.model
            )
            class_ = instance.__class__
            link += f"?{class_._meta.model_name}__id__exact={instance.id}"

            template =\
                """
                <a href="{link}"> {title}
                    <br>
                    <p class="fas fa-external-link-alt"></p>
                </a>
                """

            return django.utils.html.format_html(
                title=function(self, related_object),
                format_string=template,
                link=link
            )
        
        default_wrapper.short_description  = short_description
        
        if empty_value is not None:
            default_wrapper.empty_value_display = empty_value
        
        default_wrapper.allow_tags = True

        return default_wrapper
    
    return wrapper_of_wrapper


def to_change_link(
        short_description: typing.AnyStr,
        attribute: typing.AnyStr,
        empty_value: str = None,
        boolean: bool = None,
        ordering: str = None
    ) -> typing.Callable:

    def wrapper_of_wrapper(function: typing.Callable)\
        -> typing.Callable:

        def default_wrapper(self, 
                instance: django.db.models.Model
            ) -> typing.Any:
            related_object = getattr(instance, attribute, None)
            if not related_object:
                return empty_value
            
            link = utils.functions.change_form.admin_change_form(
                instance=related_object
            )

            template =\
                """
                <a href="{link}"> {title}
                    <br>
                    <i class="fas fa-link"></i>
                </a>
                """

            return django.utils.html.format_html(
                title=function(self, related_object),
                format_string=template,
                link=link
            )
        
        default_wrapper.short_description  = short_description
        
        if empty_value is not None:
            default_wrapper.empty_value_display = empty_value
        
        if ordering is not None:
            default_wrapper.admin_order_field = ordering

        if boolean is not None:
            default_wrapper.boolean = boolean
        
        default_wrapper.allow_tags = True

        return default_wrapper
    
    return wrapper_of_wrapper