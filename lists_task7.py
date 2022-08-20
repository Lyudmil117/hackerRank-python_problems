list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#when you have NESTED LISTS, that is how you can deal with indexes
#understand indexing
#list1[0] = 10
#list1[1] = 20
#list1[2] = [300, 400, [ 5000, 6000], 500]
#list[2][0] = 300
#list[2][1] = 400

#list1[2][2] = [5000, 6000]
#list1[2][2][0] = 5000
#list1[2][2][1] = 6000

#solution
list1[2][2].append(7000)
print(list1)
