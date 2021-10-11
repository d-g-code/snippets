# [expression for element in list]

# basic concept
print([x for x in range(0, 3)])
print([[[x, y] for x in range(0, 3)] for y in range(3, 6)])
print([[[[x, y, z] for x in range(0, 3)] for y in range(3, 6)] for z in range(6, 9)])

# list comprehension vs for loop
loop_for = []

for letter in "loop for":
    loop_for.append(letter)

print(loop_for)

list_comprehension = [letter for letter in 'Comprehension']
print(list_comprehension)

# list comprehensions vs lambda functions
lambda_function = list(map(lambda x: x, 'lambda'))
print(lambda_function)

# conditionals in list comprehension
numbers_list = [x for x in range(20) if x % 2 == 0]
print(numbers_list)

numbers_list_2 = [1, 5, -20, -2, 4, 13, 20]
print([i for i in numbers_list_2 if i >= -3 if i <= 3])

# if...else with list comprehension
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)

# expression and function in the list comprehensions
print([i.upper() for i in 'AbcDeFgHiJ'])

# transpose of a matrix using nested loops
transposed = []
matrix = [[1, 3, 5, 7], [2, 4, 6, 8]]
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# transpose of matrix using list comprehension
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = [[[row[i] for row in matrix]] for i in range(2)]
print(transpose)

# transpose of matrix using for loop
matrix = [[1, 2, 3], [11, 22, 33], [111, 222, 333]]

print([i for row in matrix for i in row])

transpose_result = []
for i in matrix:
    for row in i:
        transpose_result.append(row)
print(transpose_result)

# list comprehension use memory it is good for small or medium-sized list,
# when large list (1 billion) list comprehension should be avoid,
# better alternative for such large list is using a generator

# print([[x*x*x] for x in range(0, 10000000)])
# for x in range(0, 10000000):
#     print(x*x*x)
# def generator():
#     for x in range(0, 10000000):
#         yield x*x*x
# gen = generator()
# for ele in gen:
#     print(ele)
