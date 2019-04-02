'''
Improve the decorator from the previous exercise by allowing it to take
a tag as an input - making it more general.

'''
def p_tagging(func):
    ''' wrap text in func in <p></p> tags'''
    def wrapper(*args, **kwargs):
        for x in args:
            if x in ["p","q","div","h1", "h2"]:
                return f'<{x}>{func(*args, **kwargs)}</{x}>'
    return wrapper

@p_tagging
def func(name, tag):
    return f"In {tag} tag: {name} is in bali!"

print(func("martin","div"))