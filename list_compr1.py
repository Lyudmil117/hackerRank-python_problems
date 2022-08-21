nums = [i for i in range(1, 1001)]

string1 = "Practice Problems to Drill List Comprehension in Your Head"

#print the numbers divisibbe by 8 in nums
nums8 = [x for x in range(1, 1001) if x % 8 == 0]
print(nums8)

#find all the numbers in nums that have 6 in them

nums6 = [x for x in range(1, 1001) if "6" in str(x)]
print(nums6)

#count string spaces in the string above

count = len([char for char in string1 if char == " "]) #That was interesting was to count the spaces using LEN function
print(count)

#remove all the vowels in  string1

vowels_list = ["a", "o", "e", "i", "u"]
no_vowels = [word for word in string1 if word not in vowels_list]
no_vowels = "".join(no_vowels)
print(no_vowels)

#find all the words in string1 less than 5 chars long

new_list = string1.split(" ")
short_words = [word for word in new_list if len(word) < 5]
print(short_words)

 