list1 = [5, 20, 15, 20, 25, 50, 20]
#we want to remove 20 from the list. This how i did it.

for x in list1:
    list1.count(x)
    if x == 20:
        list1.remove(20)

print(list1)
