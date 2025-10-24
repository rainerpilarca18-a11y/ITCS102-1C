name = input("Enter your name --> ")
print("welcome to the odd number compiler.")
print("Type 0 to terminate")

odd = 0
num = True 
total = " "

while num == True :
    number = eval(input("Enter an number:  "))

    if number % 2 == 1:
        print("ODD NUMBER DETECTED")
        odd += number
        total += str(number) + " "
        print(f"{number} is an odd number and has been added to the list.")
        continue

    elif number == 0:
        print("Loop Terminated")
        print("The sum of the odd numbers: ",odd)
        print("The odd numbers are: ", total)
    
    else:
        print("EVEN number detected")