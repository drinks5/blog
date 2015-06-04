import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()  

@register.filter(is_safe=True)  
@stringfilter  
def custom_markdown(value):
    extensions = ["nl2br", ]  #insert a <br> in eachline that linefeed
    return mark_safe(markdown.markdown(force_unicode(value),
                                       extensions,
                                       safe_mode=True,
                                       enable_attributes=False))
#def custom_markdown(value):
 #   return mark_safe(markdown.markdown(value,
  #      extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
   #                                    safe_mode=True,
    #                                   enable_attributes=False))
