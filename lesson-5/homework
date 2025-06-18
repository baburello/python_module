#1 Leap year 
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
        return('Leap year')
    else:
        return('Not a leap year')

try:
    year = int(input("Enter a year: "))
    print(is_leap(year))
except ValueError:
    print("Not a valid input. Please enter a number.")

# 2
n = int(input('Enter a number'))
if n < 1 or n > 100:
    print('Enter numbers between 1 and 100')
elif n % 2 == 1:
    print('Weird')
elif n % 2 == 0 and 2 <= n <= 5:
    print('Not weird')
elif n % 2 == 0 and 6 <= n <= 20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not weird')

#3
#first way
a = int(input('Enter number a'))
b = int(input('Enter number b'))

if a > b:
    print('a can not be greater than b')
else:
   if a % 2 != 0:
       a = a + 1

even_numbers = list(range(a,b+1,2))
print('Even numbers between a and b:', even_numbers)

#second way without conditionals
a = int(input("Enter a: "))
b = int(input("Enter b: "))

start = min(a, b)
end = max(a, b)

start += start % 2  

print("Even numbers:", list(range(start, end + 1, 2)))
