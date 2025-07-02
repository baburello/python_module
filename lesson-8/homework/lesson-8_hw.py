#Exception Handling Exercises

#1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    a = 15/0
    print(a)
except ZeroDivisionError:
    print('You can not devide by 0')

#2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
str_input = input('Enter a number...')
try:
    print(int(str_input))
except ValueError:
    print('Not a valid integer')

#3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    a = open('hw2.py')
    data  = a.read()
    print(data)
except FileNotFoundError:
    print('File not found')


#4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
num1 = input('Enter num 1: ')
num2 = input('Enter num 2: ')

try:
    print('num 1 =',int(num1))
    print('num 2 =',int(num2))
except ValueError:
    raise TypeError("Invalid input: expected a number")


#5.Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    with open('/Users/boburmirzobobojonov/Courses/python_hw/test_permission.txt', 'w') as f:
        f.write('Hello World 2!')
except PermissionError:
    print('You don\'t have permission to write to this file')


#6.Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
colors = ['yellow', 'blue', 'green', 'grey', 'red']
try:
    print(colors[6])
except IndexError:
    print('The index is out of range')

#7.Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    number = int(input('Enter a number...'))
    print(number)
except KeyboardInterrupt:
    print('keyboard interrupt error you pressed ctrl + c')

#8.Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    result = 10.0 ** 10000  # extremely large
except ArithmeticError:
    print("An arithmetic error occurred")

#9.Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    with open('/Users/boburmirzobobojonov/Courses/python_hw/test_permission.txt') as f:
       content = f.read()
       print(content)
except UnicodeDecodeError:
    print('Encoding issue')

#10.Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    basic_text = 'Hello John'
    basic_text.push()
except AttributeError:
    print('There is no such method')

#example with list
try:
    my_list = [1, 2, 3]
    my_list.upper()  # list has no method 'upper'
except AttributeError:
    print('There is no such method')

# 2nd part File input

#1.Write a Python program to read an entire text file.
with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as f:
    data = f.read()
print(data)

#2.Write a Python program to read first n lines of a file.
n = int(input('Enter number of lines to read: '))
with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as f:
    for i in range(n):
        data = f.readline()
        if data == '': #meaning end of file
            break
        print(data.strip()) 

#3.Write a Python program to append text to a file and display the text.

text = 'Elephant'

with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt', 'a') as f:
    data = f.write(text + '\n')
with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as f:
    data = f.read()
    print(data)

#4.Write a Python program to read last n lines of a file.

n = int(input('Enter number of lines to read: '))
with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as f:
      data = f.readlines()
for i in data[-n:]:
      print(i.strip())

#5.Write a Python program to read a file line by line and store it into a list.
animals = []
with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as f:
    for line in f:
        animals.append(line.strip())
print(animals)

#6.Write a Python program to read a file line by line and store it into a variable.
animals = ""

with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as f:
    for line in f:
        animals += line
print(animals)

#7.Write a Python program to read a file line by line and store it into an array.
animals = []
with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as f:
    for line in f:
        animals.append(line.strip())
print(animals)


#8.Write a Python program to find the longest words.
words = ['table', 'tank', 'experience', 'boring', 'book']
longest = max(words, key=len)
print(longest)

#9.Write a Python program to count the number of lines in a text file.

lines = 0

with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as f:
    for line in f:
        lines += 1
print('Total number of lines: ' + lines)

#10.Write a Python program to count the frequency of words in a file.
# import string

word_counts = {}
with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as f:
    for line in f:
        clean_line = line.translate(str.maketrans('','', string.punctuation)).lower()
        words = clean_line.split()

        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
for word, count in word_counts.items():
    print(f"{word}: {count}")

#11. Write a Python program to get the file size of a plain file.
import os
file_size = os.path.getsize('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt')
print('File size:', file_size, 'bytes')

#12. Write a Python program to write a list to a file.

fishes = ['catfish', 'carp', 'goldfish', 'salmon', 'tuna']

with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt','w') as f:
    for fish in fishes:
       data = f.write(fish + '\n')

#13. Write a Python program to copy the contents of a file to another file.
with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as animals, open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/wild_animals.txt', 'a') as wild_animals:
    for line in animals:
        wild_animals.write(line)

#14. Write a Python program to combine each line from the first file with the corresponding line in the second file.
with open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/animals.txt') as fishes, open('/Users/boburmirzobobojonov/Courses/python_hw/hw_8/wild_animals.txt') as wild_animals:
    for fish, wild_animal in zip(fishes, wild_animals):
        combined = fish.strip() + '--' + wild_animal.strip()
        print(combined)
