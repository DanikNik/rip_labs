from lab2.librip.gens import gen_random
from lab2.librip.iterators import UniqueIterator

data1 = ['1', '1', '1', '1', 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

if __name__ == '__main__':
    i1 = UniqueIterator(data1)
    i2 = UniqueIterator(data2)

    print([e for e in i1])
    print([e for e in i2])