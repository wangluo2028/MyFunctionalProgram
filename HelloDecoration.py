#coding:utf-8

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-12-29-09-36')

#f = now
#print(f())

#print(now.__name__)
#print(f.__name__)

now()


