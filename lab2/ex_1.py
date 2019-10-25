from lab2.librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

if __name__ == '__main__':
    print([e for e in field(goods, "title")])
    print([e for e in field(goods, "title", "price")])

    print([a for a in gen_random(1, 3, 5)])
