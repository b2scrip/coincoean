from django import template
register = template.Library()

@register.filter
def tag_it(instance):
    tag_html = ''
    _tags  = instance.tags.split(";")[1::2]
    if _tags:
        try:tags = [x.split("&")[0] for x in _tags]
        except Exception:tags=[]
    if tags:
        for tag in tags:
            tag_html  += '''<a class="ui tag label">%s</a>''' % tag
        return tag_html

    
