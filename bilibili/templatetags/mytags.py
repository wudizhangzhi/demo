# -*- coding:utf8 -*-
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


# def indexnum(count, pagesize, page_cur):
def indexnum(*args):
    print(args)
    # return count + pagesize * (page_cur - 1)
    return '1'


register.tag('indexnum', indexnum)


@stringfilter
def truncatehanzi(value, arg):
    """
    Truncates a string after a certain number of words including
    alphanumeric and CJK characters.
    Argument: Number of words to truncate after.
    """
    try:
        bits = []
        for x in arg.split(u':'):
            if len(x) == 0:
                bits.append(None)
            else:
                bits.append(int(x))
        if int(x) < len(value):
            return value[slice(*bits)] + '...'
        return value[slice(*bits)]

    except (ValueError, TypeError):
        return value  # Fail silently.


register.filter('truncatehanzi', truncatehanzi)
