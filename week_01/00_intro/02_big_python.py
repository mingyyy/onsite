'''
Write the necessary code to print the following to the console:

    PPPP   Y     Y  TTTTTTTTT  H    H      O     N       N
    P   P   Y   Y       T      H    H     O O    N N     N
    P   P    Y Y        T      H    H    O   O   N  N    N
    PPPP      Y         T      HHHHHH    O   O   N   N   N
    P         Y         T      H    H    O   O   N    N  N
    P         Y         T      H    H     O O    N     N N
    P         Y         T      H    H      O     N       N

'''
p = ["  PPPP   ", "  P   P  ", "  P   P  ", "  PPPP   ", "  P      ", "  P      ", "  P      "]
y = ["Y     Y  ", " Y   Y   ", "  Y Y    ", "   Y     ", "   Y     ", "   Y     ", "   Y     "]
t = ["TTTTTTTTT", "    T    ","    T    ","    T    ","    T    ","    T    ","    T    "]
h = ["  H    H ", "  H    H ", "  H    H ","  HHHHHH ","  H    H ","  H    H ","  H    H "]
o = ["    O   ", "   O O  ", "  O   O ", "  O   O ", "  O   O ", "   O O  ", "    O   "]
n = [" N       N", " N N     N", " N  N    N", " N   N   N", " N    N  N"," N     N N", " N       N" ]

for i in range(7):
    print(str(p[i])+ str(y[i])+ str(t[i])+ str(h[i])+ str(o[i])+ str(n[i]))
