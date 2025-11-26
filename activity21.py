import random
random_value = random.randint(1,5)
tries = 0 
yolut = True
name=input("What is your name? ")
while yolut == True:
    num = eval(input("Give a number:  "))
    tries += 1
    if num == random_value:
        print("Winner")
        break
    else:
        print(" incorrect")
        continue

print(f"Hi,{name},Your number of tries is {tries}")