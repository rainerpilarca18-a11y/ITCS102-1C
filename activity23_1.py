def greetname(name):
    print(f"Hi,{name}, welcome to the earth")

def greetperson(name,loc,age):
    print(f"Hi,{name},located at{loc},{age} years old")

def sumnum(number):
    print(f"The summation of 1 + {number}")
    sum = 0
    for x in range(1, number + 1,1):
        sum += x
    return sum

def factorial(number):
    print(f"the factorial of {number}")
    fact = 1
    for x in range(number,1,-1):
        fact *= x
    return fact