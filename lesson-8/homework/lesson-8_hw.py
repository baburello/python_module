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
