# https://www.spoj.com/problems/PRIME1/
test_cases = int(input())
prime_number = []


def check_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    prime_number.append(number)


for test in range(test_cases):
    numbers = input()
    m = int(numbers[:numbers.rfind(' ')])
    n = int(numbers[numbers.rfind(' ')+1:])
    for number in range(m, n+1):
        if number <= 1:
            continue
        check_prime(number)
    prime_number.append(' ')

for i in range(len(prime_number)):
    print(prime_number[i])
