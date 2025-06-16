#1.Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'apple': 10, 'banana': 5, 'cherry': 15, 'date': 7}
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order:", ascending)
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", descending)

#2. Write a Python script to add a key to a dictionary.
nums = {
    0: 10,
    1: 20
    }
nums[2] = 30
print(nums)

#3. Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

#first way
merged = {**dic1, **dic2, **dic3}
print(merged)

#second way
merged_dic = {}
for d in dic1,dic2,dic3:
    merged_dic.update(d)
print(merged_dic)

#4.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#Sample Dictionary (n = 5):

n = int(input("Enter a number: "))

# Generate the dictionary
squares_dict = {x: x * x for x in range(1, n + 1)}

# Print the result
print(squares_dict)

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#5. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

squares_dict = {}
for i in range(1,16):
    squares_dict[i] = i*i

print(squares_dict)

#SET
#1. Write a Python program to create a set.
set() #empty set
numbers_set = {1, 2, 3, 4, 5} # Creating a set with some values

#2. Write a Python program to iterate over sets.
numbers_set = {1,2,3,4,5}
for i in numbers_set:
    print(i)

#3. Write a Python program to add member(s) to a set.
thisset = {"apple", "banana", "cherry"}
thisset.add("apricot")
print(thisset)

#4. Write a Python program to remove item(s) from a given set.
fruits_set = {"apple", "banana", "cherry"}
fruits_set.remove("cherry")
print(fruits_set)

#5. Write a Python program to remove an item from a set if it is present in the set.
veg_set = {"carrot", "tomato", "cucumber"}
if "cucumber" in veg_set:
    veg_set.remove("cucumber")
else:
    print("not in the set")
print(veg_set)
