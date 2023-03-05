from django.utils.html import strip_tags

def brief_description_pre_save(sender, instance, *args, **kwargs):
    if not instance.brief_description:
        instance.brief_description = strip_tags(instance.detail)