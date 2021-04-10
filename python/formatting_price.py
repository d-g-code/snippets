"""
Formatting string to price form.
"""


def formatting_price(price):
    price_int = int(price) / 100
    price_str = str(price_int).replace('.', ',')
    if int(price) > 99999:
        price_list = list(price_str[::-1])
        index = 3
        while len(price_list) > index + 3:
            price_list.insert(index + 3, ' ')
            index += 4
        price_list.reverse()
        s = ''
        print(s.join(price_list))
    else:
        print(price_str)
