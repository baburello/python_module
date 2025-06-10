#1. Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
import datetime
user_name = input('What is your name?')
birth_year = int(input('What is your birth year?'))
current_date = datetime.datetime.now().year
age = current_date - birth_year
result = f'{user_name} is {age} years old'
print(result)

#2. Extract car names from the following text:
txt = 'LMaasleitbtui'
car_name1 = txt[::2]
print(car_name1) #Lasetti
car_name2 = txt[1::2]
print(car_name2) #Malibu

#3. Extract car names from the following text:
txt = 'MsaatmiazD'
car1 = txt[::2]
car2 = txt[::-2]
print(car1)
print(car2)

#4. Extract the residence area from the following text:
txt = "I'am John. I am from London"
words = txt.split()
residence = words[5]
print(residence)

#5. Write a Python program that takes a user input string and prints it in reverse order.
user_input = input('Write some text to get it reversed!')
reverse = user_input[::-1]
print(reverse)

#6.Write a Python program that counts the number of vowels in a given string.
text = input('Enter text to get vowel count...')
vowels = 'aeiouAEIOU'
count = 0

for char in text:
    if char in vowels:
        count +=1
        
result = f'The number of vowels in the string "{text}" is: {count}'
print(result)

#7. Write a Python program that takes a list of numbers as input and prints the maximum value.
numbers_as_string = input('Enter numbers separated by commas (e.g., 10,5,20): ')
list_of_string_numbers = numbers_as_string.split(',')
list_of_actual_numbers = []
for number_str in list_of_string_numbers:
    integer_number = int(number_str)
    list_of_actual_numbers.append(integer_number)
maximum_value = max(list_of_actual_numbers)
print(f"The maximum number is: {maximum_value}")

#8.Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
input_text = input('check polindrome...')
print(input_text == input_text[::-1])

#9. Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input('enter your emai here...')
if '@' in email:
    email_domain = email.split('@')[1]
    print(email_domain)
else:
    print('Invaid email')

#10. Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

def generate_password(length=12):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    special_chars = string.punctuation  # !@#$%^&*()_+ etc.
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]
    all_chars = letters + digits + special_chars
    password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)
    return ''.join(password)

print("Generated password:", generate_password(12))










