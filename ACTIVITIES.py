# WHILE LOOP LAB ACT 2
# Sum of Even Numbers
number = int(input("Enter a number: "))
summation = 0
number_of_run = 0

while number_of_run <= number:
  number_of_run += 1
  if number_of_run % 2 == 0:
    summation += number_of_run
    print(summation, "+", number_of_run)

# || ========================================================================== || #

# WHILE LOOP LAB ACT 2
# Factor Finder
number_to_factor = int(input("Enter a number to factor out: "))

number_of_run = 0

while number_of_run <= number_to_factor:
  number_of_run += 1

  factor = number_to_factor % number_of_run

  if factor == 0:
    print(number_of_run)

# || ========================================================================== || #

# WHILE LOOP LAB ACT 2
# Simple ATM Menu
print("ATM MENU:")
print("1 - Deposit")
print("2 - Withdraw")
print("3 - Check Balance")
print("4 - Exit")
print("")

balance = 10000

while True:
  atm_inp = int(input("Enter a number for the menu of the ATM machine: "))

  match atm_inp:
    case 1:
      atm_inp = int(input("Enter amount to deposit: "))
      print("You have deposited", atm_inp, "into your account")
      balance += atm_inp
      print("Your balance is now", balance)

    case 2:
      atm_inp = int(input("Enter amount to withdraw: "))

      if balance >= atm_inp:
        balance -= atm_inp
        print("You have withdrawn", atm_inp, "your balance is now", balance)
      else:
        print("Insufficient funds in your account")

    case 3:
      print("Your balance is", balance)
      print("")
      atm_inp = int(input("Enter another number for the ATM machine: "))

    case 4:
      print("Exit")
      break

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# Print 1 to 20
for i in range(1, 21):
  print(i)

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# Even numbers
for i in range(1, 41):
  if i % 2 == 0:
    print(i)

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# Sum of first 10 numbers
summation = 0

for i in range(1, 11):
  summation += i
  print(summation)

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# Print Characters in a Word
word = str(input("Enter a word: "))

for character in word:
  print(character)

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# Multiplication Table (1 to 10)
number = int(input("Enter a number: "))

for i in range(1, 11):
  print(number, "x", i, "=", number * i)

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# Factorial Calculator
number = int(input("Enter a number to compute its factorial: "))

for i in range(1, number + 1):
  if number % i == 0:
     print(i)

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# Count Vowels in a String
string = str(input("Enter a word: "))
summation = 0
vowels = "aeiouAEIOU"

for vowel in string:
  if vowel in vowels:
    summation += 1

print("There are", summation, "vowels in the string you gave")

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# Reverse a word
string = str(input("Enter a word: "))
print(string[::-1])

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# Squares of a number
number_to_square = int(input("How many numbers should we square? (1-50): "))

print("")

for number in range(1, number_to_square + 1):
    print(number, "when squared is:", number ** 2)

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# pattern printing
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)

print('')

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# prime number checker
number = int(input("Enter a number: "))

if number < 2:
      print(number, "is not a prime number")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# || ========================================================================== || #

# FOR LOOP LAB ACT 2
# sum of digits
number_input = int(input("Enter a number: "))
string_version = str(number_input)
sum = 0

for digit in string_version:
  sum += int(digit)

print("Sum of the digits in the number is:", sum)
