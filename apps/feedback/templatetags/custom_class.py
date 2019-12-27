from django import template

register=template.Library()

@register.filter(name='customcls')
def customcls(field,css):
    return field.as_widget(attrs={"class":css})