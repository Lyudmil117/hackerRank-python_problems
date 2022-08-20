numbers = [1, 2, 3, 4, 5, 6, 7]

output = [x ** 2 for x in numbers]
#or longer way
list_square = []
for x in numbers:
    y = x**2
    list.append(y)


print(output)
print(list_square)