#
# Wczytaj ciąg liczb. Następnie wypisz wczytane liczby w taki sposób, aby najpierw pojawiły się te, które wystąpiły na pozycjach parzystych, a następnie te, które wystąpiły na pozycjach nieparzystych; z zachowaniem pierwotnej kolejności w obrębie obu grup. Numerujemy od 1.
# Wejście
#
# Najpierw t - liczba testów. Następnie dla każdego testu liczba n i n liczb, n <= 100.
# Wyjście
#
# Dla każdego testu n liczb w opisanym porządku.
# Przykład
#
# Wejście:
# 2
# 4 1 2 3 5
# 3 9 8 7
#
# Wyjście:
# 2 5 1 3
# 8 9 7

tests = int(input("How many tests "))

while tests > 0:
    n = int(input("How many numbers "))

    list_in = []
    list_out = []
    for c in range(n):
        list_in.append(int(input("Take a numbers ")))
    for a in list_in:
        x = list_in.index(a)
        if (x % 2) == 0:
            list_out.append(a)
    for b in list_in:
        y = list_in.index(b)
        if (y % 2) != 0:
            list_out.append(b)
    list_out.pop(0)
    print(list_out)
    tests -= 1
