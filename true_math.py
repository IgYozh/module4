from math import inf

def divide(first, second):
    result = 0
    if second == 0:
        result = inf
        return result
    else:
        result = first/second
        return result
