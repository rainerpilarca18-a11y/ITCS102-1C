amount = eval(input ("Enter amount to deposit... "))
print ("Here is the breakdown of your deposit:")
n1 = amount //1000
print(n1, "\t - \t1000")
amount = amount % 1000
n2 = amount //500
print(n2, "\t - \t500")
amount = amount % 500
n3 = amount // 200
print(n3, "\t - \t200")
amount = amount % 200
n4 = amount // 100
print(n4, "\t - \t100")
amount = amount % 100
n5 = amount // 50
print(n5, "\t - \t50")
amount = amount % 50
n6 = amount // 20
print(n6, "\t - \t20")
amount = amount % 20
n7 = amount // 10
print(n7, "\t - \t10")
amount = amount % 10
n8 = amount // 1 
print(n8, "\t - \t1")
amount = amount % 1