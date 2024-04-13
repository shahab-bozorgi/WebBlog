from django.template import Library

register = Library()


@register.inclusion_tag('home_app/result.html')

def show_result(text):
    return {'text': text}