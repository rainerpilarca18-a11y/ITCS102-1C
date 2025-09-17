number = eval(input("Enter a number to multiply: "))

for i in range(1,11, 1):
	total = i * number
	print(number, "x", i,"=", total)