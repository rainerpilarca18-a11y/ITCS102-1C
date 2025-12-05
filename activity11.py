temp = float(input("Enter temperature -->"))

if temp >= 1 and temp <= 20:
    print("Freezing Cold.")

elif temp >= 21 and temp <= 30:
    print("Cold")

elif temp >= 31 and temp <= 37:
    print("Normal")

elif temp >= 38 and temp <= 45:
    print("Hot")\
    
elif temp >= 45  and temp <= 50:
    print("Very Hot!")

elif temp > 50:
    print("Dangerously Hot!!")

else:
    print("Invalid Input")