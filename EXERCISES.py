# Exercise 1: Multiplication Table Generator
number = int(input("Enter a number from 1-10: "))

for i in range(1, 11):
  nn = i * number
  print(number, "x", i, "=", nn)

# Exercise 2: Sum of Even Numbers (1 to N)
number = int(input("Enter a number: "))

for i in range(1, number):
  nn = i * number
  print(number, "x", i, "=", nn)

# Exercise 3: Star Pattern Pyramid
rows = int(input("Enter number of rows: "))

for i in range(1, rows):
  print("*" * i)



# Exercise 4: Number Guessing Game
import random
min_num = 1
max_num = 15
number_to_guess = random.randint(min_num, max_num)
input_from_user = 0

while input_from_user != number_to_guess:
    input_from_user = int(input("Enter a number from 1-15:"))

    if input_from_user > number_to_guess:
        print('Too High! Try Again')
    elif input_from_user < number_to_guess:
        print('Too Low! Try Again')
    else:
        print('Correct!')

# Exercise 5: Running Total Calculator

total = 0
num = 1

while num != 0:
    num = int(input('Enter a number (0 to exit): '))
    print("Added", num, "to your summation")
    total += num

print("Your total is:", total)

# Exercise 6: Login Attempt Limiter

password = 'PotatoPcPotatoProgrammer'
user_attempts = 0

while user_attempts < 3:
    password = input('Enter your password: ')

    if password == password:
        print('Login Successful!')
        break
    else:
        print('Incorrect Password')
        user_attempts += 1

if user_attempts == 3:
    print('Account Locked')
