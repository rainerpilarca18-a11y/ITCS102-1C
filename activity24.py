from activity23_1 import *

print("Welcome to my program")
name = input("What is your name? ")
print(f"hello, {name}, select an option")
print("A- greet name\nB - greet with name, age, loc \nC- sum \nD- factorial")

isCont = True

while isCont == True:
    choice = input("Select A to D ---- ").lower()

    if choice == 'a':
        name = input("What is your name?")
        greetname(name)
        continue
    elif choice == 'b':
        namegreet = input("What is your name, age, and location")
        greetperson(namegreet)
        continue

    else:
        print("invalid input try again")
        continue
