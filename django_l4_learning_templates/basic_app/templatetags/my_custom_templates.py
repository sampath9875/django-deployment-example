from django import template

register = template.Library()

@register.filter(name='cut_me')
def cut_me(value,arg):
    """
    This cuts out all the values of "arg" from the string
    """
    return value.replace(arg,'')

# register.filter('cut_me',cut_me)