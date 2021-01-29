import math
import time
from fractions import *
print("This was created by Brady Van Oss you may download others like it at https://github.com/dawaffleman123/Math-Tools")
print("Welcome to the Slope Formula Calculator")
while True:
    X1 = int(input("What is x1? "))
    X2 = int(input("What is x2? "))
    Y1 = int(input("What is y1? "))
    Y2 = int(input("What is y2? "))
    X3 = X2 - X1
    Y3 = Y2 - Y1
    print()
    print("Work")
    print("      "+str(Y2) + " - " + str(Y1))
    print("M = ------------")
    print("      "+str(X2) + " - " + str(X1))
    print()
    print("      " + str(Y3))
    print("M = ------------")
    print("      " + str(X3))
    print()
    print(Fraction(Y3, X3))
    time.sleep(1)

