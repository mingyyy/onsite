'''
Write a script with a function that demonstrates the use of **kwargs.

'''


from datetime import datetime, date


def visitor_registration( **kwargs):
    v_date = date.today()
    result = f"On {v_date}, visitor info as follows:\n"
    for k, v in kwargs.items():
        result += f"{k.capitalize()}: {v}\n"
    return result


v = visitor_registration(martin = "A lovely place", michael = "What a hot day.")
print(v)
