sum = 0
for x in range(1,11,1):
    print(x)
    number = eval(input("Enter the number that you want to add: "))
    sum += number
print("The sum of all the given numbers is",sum)