p = eval(input("How much?"))
q = eval(input("How many?"))

cost = p * q

if cost >= 100:
	print("You have a discount of 10%")
	discount = cost * .10
	totalcost = cost - discount
	print("Your total now is, ", totalcost)
else:
	print("Your total will be, ", cost)