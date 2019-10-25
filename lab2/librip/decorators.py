import functools


def print_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        res_type = type(result)
        if res_type is list:
            for i in result:
                print(i)
        elif res_type is dict:
            for i in result.items():
                print(f'{i[0]}={i[1]}')
        else:
            print(result)
        return result

    return wrapper
