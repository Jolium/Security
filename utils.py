from timeit import default_timer as timer


def time_func(func):
    def inner(*args, **kwargs):
        start = timer()
        results = func(*args, **kwargs)
        end = timer()
        message = f'{func.__name__} took {end - start} seconds!'
        print(message)
        return results
    return inner
