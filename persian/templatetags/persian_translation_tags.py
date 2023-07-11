from django import template


register = template.Library()

@register.filter
def num_to_persian(value):
    value = str(value)
    eng_to_per = value.maketrans('0123456789','۰۱۲۳۴۵۶۷۸۹')
    return value.translate(eng_to_per)
