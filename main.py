from operator import concat
import random
from tokenize import String
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to my password Generator!")
print('''
        Here You can Generate Your password 
           In Your Own choice ''')
nr_letters=int(input("Enter Number of letter You Want to choose\n") )
nr_numbers=int(input("Enter Number of Number You Want to choose\n") )
nr_symbols=int(input("Enter Number of symbol You Want to choose\n") )
i=0
first_letter=letters[random.randint(0,25)]
while i < nr_letters-1:
  first_letter=first_letter+letters[random.randint(0,25)]
  i=i+1
i=0
first_symbols=symbols[random.randint(0,8)]
while i < nr_symbols-1:
  first_symbols=first_symbols+symbols[random.randint(0,8)]
  i=i+1
i=0
first_numbers=numbers[random.randint(0,8)]
while i < nr_numbers-1:
  first_numbers=first_numbers+numbers[random.randint(0,8)]
  i=i+1

print(first_letter+first_symbols+first_numbers)
  
user_input=input("For More Strong Password press y if want and if Not press n==>")
if user_input =='n':
  print("Thanks to use our service please visit again")
  exit()
else:
  print("Thanks for comming in our advanced servise we will try to best serve you")
  strong_pass_num=int(input("Number of digits you want in your password==>"))
  pass_list=list((letters,numbers,symbols))
  password=''
  i=0
  while i < strong_pass_num:
    choice_first=random.choice(pass_list)
    password=random.choice(choice_first)+password
    i+=1
  print(password)
