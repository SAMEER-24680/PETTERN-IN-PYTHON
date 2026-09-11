print("HALF PYRAMID PATTERN OF STARS (*) : ")
a = int(input("ENTER THE NUMBER OF ROWS YOU WANT TO DISPLAY : "))
for i in range(a):
    for b in range(i+1):
        print(" * ", end = "")
    print( )
    continue