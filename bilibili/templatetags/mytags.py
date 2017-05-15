# -*- coding:utf8 -*-
from django import template

register = template.Library()


# def indexnum(count, pagesize, page_cur):
def indexnum(*args):
    print args
    # return count + pagesize * (page_cur - 1)
    return '1'


register.tag('indexnum', indexnum)
