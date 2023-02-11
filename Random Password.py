# This program creates password for users based on their priorities
import random
import string
print("This program creates password for you based on your priorities.")
a=int(input("please enter password lenght (8-15 digits): "))
if a<8 or a>15: 
    print("Error.Enter a number between 8 and 15 next time.")
    exit()
b=int(input("please enter the number of uppercase letters (at least one): "))
c=int(input("please enter the number of digits (at least one): "))
d=int(input("please enter the number of lowercase letters (at least one): "))
specialcharacter =["/","*","-","+","=","@","&","£","?"]
if b>a or c>a or d>a or a<0 or b<0 or c<0 or d<0:
   print("You entered wrong data. Please try again")
   exit()
if a<b+c+d-1:
    print("You entered the wrong number of password lenght.\n Your password will be built based on our policy.")
    a=b+c+d+1
if b+c+d>14:
    print("You entered the wrong number of characters' lenght.\nYour password will be built based on our policy.")
    upperletters = random.choices(string.ascii_uppercase, k=3)
    digits = random.choices(string.digits, k=3)
    lowerletters = random.sample(string.ascii_lowercase, k=3)
    special = random.sample(specialcharacter, k=3)
    selectedpass = upperletters + digits + lowerletters + special
    print("We choose this password for you: " , selectedpass )
else:
    upperletters = random.choices(string.ascii_uppercase, k=b)
    digits = random.choices(string.digits, k=c)
    lowerletters = random.sample(string.ascii_lowercase, k=d)
    special = random.sample(specialcharacter, k=a-b-c-d)
    password = upperletters + digits + lowerletters + special
    print("pasword: " ,password ) 

