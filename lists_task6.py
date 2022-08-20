list1 = ["Mike", "", "Emma", "Kelly"]
#print new list,without the empty strings

new = [x for x in list1 if x != ""]
# Or the longer way
list2 = []
for x in list1:
    if x != "":
        list2.append(x)
print(new)
print(list2)
