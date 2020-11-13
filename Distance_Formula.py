import math
import time
print("This was created by Brady Van Oss you may download others like it at https://github.com/dawaffleman123/Math-Tools")
print("Welcome the the Distance Formula calculator")
while True:
    X1 = int(input("What is x1? "))
    X2 = int(input("What is x2? "))
    Y1 = int(input("What is y1? "))
    Y2 = int(input("What is y2? "))
    X3 = X2 - X1
    X4 = X3 * X3
    Y3 = Y2 - Y1
    Y4 = Y3 * Y3
    Dis = int(X4) + int(Y4)
    print(" ")

    print("The Distance is: " + str(Dis))
    print("The Square root is: " + str(math.sqrt(Dis)))
    time.sleep(3)
    
