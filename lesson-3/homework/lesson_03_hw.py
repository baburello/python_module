#1.Create a list containing five different fruits and print the third fruit.
fruits = ['apple', 'banana', 'lemon', 'peach', 'apricot']
print(fruits[2])

#2.Create two lists of numbers and concatenate them into a single list.
nums_1 = [1,2,3,4,5]
nums_2 = [6,7,8,9,10]

result = nums_1 + nums_2
print(result)

#3.Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
selected = [numbers[0],numbers[int(len(numbers)/2)],numbers[-1]]
print(selected)

#4.Create a list of your five favorite movies and convert it into a tuple.
fav_movies=['Titanic', 'Spiderman', 'James Bond', 'The Green Book', 'The Shawshank Redemption']
fav_movies_tuple = tuple(fav_movies)
print(fav_movies_tuple)

#5.Given a list of cities, check if "Paris" is in the list and print the result.
cities = ['London', 'Barcelona', 'Manchester', 'Rome', 'Paris', 'Khonka']
if 'Paris' in cities:
    print('Yes, Paris is in the list')
else:
    print('No, Paris is not in the list')

#6. Create a list of numbers and duplicate it without using loops.
nums = [10,4,54,33,999,23]
nums_copy = nums.copy()
print(nums_copy)
print(nums)

#7. Given a list of numbers, swap the first and last elements.
num_list = [99,45,32,18,77,34,81]
num_list[0],num_list[-1] = num_list[-1],num_list[0]
print(num_list)

#8. Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
nums_tup = (1,2,3,4,5,6,7,8,9,10)
print(nums_tup[3:7:])

#9. Create a list of colors and count how many times "blue" appears in the list.
colors = ['red','purple', 'blue', 'orange', 'blue', 'red', 'pink']
count = 0

for i in colors:
    if i == 'blue':
        count += 1
print(f'"blue" appears {count} times in a list of colors')

#10. Given a tuple of animals, find the index of "lion".
animals = ('cat', 'snake', 'tiger', 'bear', 'lion', 'turtule')
print(animals.index('lion'))

#11. Create two tuples of numbers and merge them into a single tuple.
numbers_1 = (4,33,99,58,90,3)
numbers_2 = (3,11,22,43,98,46)
merged_numbers = numbers_1 + numbers_2
print(merged_numbers)

#12. Given a list and a tuple, find and print their lengths.
list_example = ['doll', 4, 44, 'car',333]
tuple_example = ('cellphone', 99, 12,8)
print(len(list_example))
print(len(tuple_example))

#13. Create a tuple of five numbers and convert it into a list.
tuple_nums = (49,88,28,39,1)
list_nums = list(tuple_nums)
print(list_nums)
#14. Given a tuple of numbers, find and print the maximum and minimum values.

num_tuple = (4,98,233,85,22,84,29)
print(max(num_tuple))
print(min(num_tuple))

#15. Create a tuple of words and print it in reverse order.
words = ('bear', 'mouse', 'phone', 'mug', 'water')
reversed_words = words[::-1]
print(reversed_words)

#or another method
reversed_2 = tuple(reversed(words))
print(reversed_2)








