#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Creating empty lists
letterslist = []
numberlist = []
symbollist = []


#Creating variables that contain number of elements in each category
max_num_of_letters = len(letters) - 1
max_num_of_numbers = len(numbers) - 1
max_num_of_symbols = len(symbols) - 1

#Creating loops that append random items to the empty lists
for i in range(nr_letters):
    x = random.randint(0, max_num_of_letters)
    letterslist.append(letters[x])

for i in range(nr_numbers):
    x = random.randint(0, max_num_of_numbers)
    numberlist.append(numbers[x])

for i in range(nr_symbols):
    x = random.randint(0, max_num_of_symbols)
    symbollist.append(symbols[x])

#Creating a list containing all elements of the code
codelist = letterslist + numberlist + symbollist

#Shuffling the codelist
random.shuffle(codelist)

finalcode = ''.join(str(e) for e in codelist)

print(finalcode)


