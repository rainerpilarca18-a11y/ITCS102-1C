rows = 5

for i in range(1, rows + 1):
    for x in range(rows - i):
        print("  ", end="")
    for y in range(i, 0, -1):
        print(y, end=" ")
    for z in range(2, i + 1):
        print(z, end=" ")
    print()

for i in range(rows - 1, 0, -1):
    for x in range(rows - i):
        print("  ", end="")
    for y in range(i, 0, -1):
        print(y, end=" ")
    for z in range(2, i + 1):
        print(z, end=" ")
    print()