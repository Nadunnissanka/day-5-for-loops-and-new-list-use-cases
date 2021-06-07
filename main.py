#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = list()

for letter in range(1,nr_letters+1):
  random_integer = random.randint(0,51)
  random_letter = letters[random_integer]
  password.append(random_letter)

for symbol in range(1, nr_symbols+1):
  random_integer = random.randint(0,8)
  random_symbol = symbols[random_integer]
  password.append(random_symbol)

for number in range(1, nr_numbers+1):
  random_integer = random.randint(0,9)
  random_number = numbers[random_integer]
  password.append(random_number)

random.shuffle(password)
mypassword = ''.join(password)
print(f"Your Generated password is: {mypassword}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P