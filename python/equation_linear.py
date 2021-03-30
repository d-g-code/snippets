# https://pl.spoj.com/problems/JROWLIN/
data_input = input('Give three number separate space: ')

clean_data = data_input.split()

a = float(clean_data[0])
b = float(clean_data[1])
c = float(clean_data[2])


try:
    x = (c-b)/a
    print(round(x, 2))
except ZeroDivisionError:
    if b == c:
        print('NWR')
    else:
        print('BR')
