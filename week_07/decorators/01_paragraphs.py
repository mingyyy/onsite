'''
Write a decorator function that wraps text passed to it in <p> tags.

'''


def p_tagging(func):
    ''' wrap text in func in <p></p> tags'''
    def wrapper(*args, **kwargs):
        return f'<p>{func(*args, **kwargs)}</p>'
    return wrapper

@p_tagging
def func(name):
    return f"{name} is in bali"

print(func("martin"))