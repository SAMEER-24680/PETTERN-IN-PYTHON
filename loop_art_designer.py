print("===== STAR PYRAMID DESIGN =====")
rows = int(input("ENTER THE NUMBER OF ROWS YOU WANT TO PRINT : "))
for i in range(rows):
    for j in range(i + 1):
        print("* ", end = "")
    print()
print("===== FLOYD'S TRIANGLE =====")
rows = int(input("ENTER THE NUMBER OF ROWS FOR FLOYD'S TRIANGLE "))
number = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end = " ")
        number += 1
    print()