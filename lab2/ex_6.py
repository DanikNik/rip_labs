import json
import sys
from lab2.librip.ctxmgr import timer
from lab2.librip.decorators import print_result
from lab2.librip.gens import field, gen_random
from lab2.librip.iterators import UniqueIterator as unique

path = sys.argv[1]

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return list(unique(field(arg, "job-name"), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda s: "программист" in s, arg))


@print_result
def f3(arg):
    return list(map(lambda s: f"{s} с опытом Python", arg))


@print_result
def f4(arg):
    prof = gen_random(100000, 200000, len(arg))
    return list(map(lambda s: f'{s[0]}, зарплата {s[1]} руб.', zip(arg, prof)))


if __name__ == '__main__':
    with open(path) as f:
        data = json.load(f)

    with timer():
        f4(f3(f2(f1(data))))