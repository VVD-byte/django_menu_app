from django import template

register = template.Library()

@register.simple_tag
def menu_template(name = 1):
    if name == 1:
        return {1:1,2:2,3:3,4:4,5:5}
    else:
        return {2:2,5:5}