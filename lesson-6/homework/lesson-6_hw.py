#1 Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.

txt = input('Enter any chars:')
vowels = 'AUIOEauioe'
result = []
count = 0
i = 0

while i < len(txt):
    result.append(txt[i])
    count += 1
    
    if count == 3:
        if txt[i] in vowels or (i + 1 < len(txt) and txt[i+1] == '_'):
            count -= 1
        else:
            result.append('_')
            count = 0
    i += 1

if result and result[-1] == '_':
    result.pop()
print(''.join(result))

#2 The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

n = int(input('Enter non-negative number...'))
if n < 1 or n > 20:
    print('Please enter numbers between 1 and 20')
else:
    for i in range(n):
        print(i**2)

#3.1 Print first 10 natural numbers using a while loop

num = 0
while num < 10:
    num +=1
    print(num)

#3.2 Print the pattern

#with for
for i in range(1,6):
    for l in range(1, i + 1):
        print(l, end=' ')
    print()

#with while
rows = 1
while rows <= 5:
    i = 1
    while i <= rows:
        print(i, end=' ')
        i += 1
    print()
    rows += 1

#3.3  Calculate sum of all numbers from 1 to a given number

num = int(input('Enter a number...'))
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
print(sum)

#4.Print multiplication table of a given number

num = int(input('Enter a num'))
i = 1
while i <= 10:
    print(num*i)
    i+=1

#5. Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    print(i)

#6. Count the total number of digits in a number

num = int(input('Enter a num'))
count = 0
for i in str(num):
    count += 1
print(count)

#7.Print reverse number pattern

for i in range(5,0,-1):
    for l in range(i, 0, -1):
        print(l, end=' ')
    print()

#8. Print list in reverse order using a loop

# list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)

#9. Display numbers from -10 to -1 using a for loop

for i in range(-10, 0):
    print(i)

#10.Display message “Done” after successful loop execution

for i in range(1,11):
    print(i)
print('Done')

#11. Print all prime numbers within a range

for num in range(10, 51):  
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)

#12.  Display Fibonacci series up to 10 terms
def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n < 0:
        print('Please enter non-negative num')
    else:
        print(a)
        print(b)
    
    for i in range(2,n):
        c = a + b
        print(c)
        a = b
        b = c
fib(10)

#13.Find the factorial of a given number

num = int(input('Enter num to check its factorial: '))
factorial = 1

for i in range(1,num + 1):
   factorial = factorial * i
print(factorial)


#14.Return the elements that are not common between two lists. The order of elements does not matter.

list1 = [1, 1, 2] 
list2 = [2, 3, 4]
uncommon_list = []

for i in list1:
    if i not in list2:
            uncommon_list.append(i)
for j in list2:
      if j not in list1:
            uncommon_list.append(j)
print(uncommon_list)
