list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list3 = list(reversed(list2))
count = -1
#numbers from the first list need to be printed with number from
#list2 but in reverse order

for x in list1:
    count += 1
    print(x, list3[count])
