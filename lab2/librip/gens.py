import random


def field(val_list, *args):
    assert len(args) > 0
    for e in val_list:
        d = {}
        for a in args:
            if (a in e.keys()) and (len(args) == 1):
                yield e[a]
            elif a in e is not None:
                d[a] = e[a]
        if len(d) > 0 and len(args) > 1:
            yield d


def gen_random(beg, end, count):
    for i in range(count):
        yield random.randint(beg, end)
