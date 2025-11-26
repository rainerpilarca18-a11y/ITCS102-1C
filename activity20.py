wash = True
while wash == True:
        wash_again = input("Want to wash? ").lower()
        if wash_again == 'yes':
            print("wash again?")
            continue
        else:
            print("done washing")
        break
