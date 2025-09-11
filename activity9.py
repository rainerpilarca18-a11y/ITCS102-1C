a = 1
b = 7
c = 3
d = 8

user = 'Rainer'
password = 'iloveyou3000'

print("USER LOGIN ")
print( (user == 'Rainer') and (password == 'iloveyou3000'))

print((a > b) and (c < d))
print((a > b) or (c < d))
print(not (a < b) and (c < d))
print(not (a < b) or (c < d))

result = ((a < b) and not (c > b) or ((b == a + d and (a != d)) or (c < a)))
print(result)