from getpass import getpass

user = 'Rainer'
password = 'iloveyou123'

u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")
from getpass import getpass

if (u == user) and (p == password) :
        print("Access Granted")
else:
        print("Access Denied")
 