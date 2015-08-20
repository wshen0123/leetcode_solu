def memorize(function):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            ret = function(*args)
            cache[args] = ret
            return ret
    return wrapper
