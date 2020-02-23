from django import template

register = template.Library()

@register.filter(name='get_objects_page')
def get_objects_page(paginator, page):
    """Return page by index"""
    
    return paginator.page(page).object_list
