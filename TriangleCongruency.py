import math
print("This was created by Brady Van Oss you may download others like it at https://github.com/dawaffleman123/Math-Tools")
print("Welcome the to the triangle congruency calculator!")
print("Please enter in the values for ABC")
while True:
    #Collecting the points
    AX= int(input("What is point A(X)? "))
    BX= int(input("What is point B(X)? "))
    CX= int(input("What is point C(X)? "))
    #DX= int(input("What is point D(X)? "))
    #EX= int(input("What is point E(X)? "))
    #FX= int(input("What is point F(X)? "))
    AY= int(input("What is point A(Y)? "))
    BY= int(input("What is point B(Y)? "))
    CY= int(input("What is point C(Y)? "))
    #DY= int(input("What is point D(Y)? "))
    #EY= int(input("What is point E(Y)? "))
    #FY= int(input("What is point F(Y)? "))

    #Print the points
    print("Points for reference")
    print(" ")
    print("Point A = (" + str(AX) + "," + str(AY) + ")")
    print("Point B = (" + str(BX) + "," + str(BY) + ")")
    print("Point C = (" + str(CX) + "," + str(CY) + ")")
    #print("Point D = (" + str(DX) + "," + str(DY) + ")")
    #print("Point E = (" + str(EX) + "," + str(EY) + ")")
    #print("Point F = (" + str(FX) + "," + str(FY) + ")")
    print(" ")

    #Start the equation

    #AB
    ABX = BX - AX
    ABX2 = ABX * ABX
    ABY = BY - AY
    ABY2 = ABY * ABY
    ABDIS = int(ABX2) + int(ABY2)
    print("AB")
    print("The Distance of AB is: " + str(ABDIS))
    print("The Square root of AB is: " + str(math.sqrt(ABDIS)))
    print(" ")

    #AC
    ACX = CX - AX
    ACX2 = ACX * ACX
    ACY = CY - AY
    ACY2 = ACY * ACY
    ACDIS = int(ACX2) + int(ACY2)
    print("AC")
    print("The Distance of AC is: " + str(ACDIS))
    print("The Square root of AC is: " + str(math.sqrt(ACDIS)))
    print(" ")

    #BC
    BCX = BX - CX
    BCX2 = BCX * BCX
    BCY = BY - CY
    BCY2 = BCY * BCY
    BCDIS = int(BCX2) + int(BCY2)
    print("BC")
    print("The Distance of BC is: " + str(BCDIS))
    print("The Square root of BC is: " + str(math.sqrt(BCDIS)))
    print(" ")

    #ABC
    print("ABC")
    if int(ABDIS) == int(ACDIS) == int(BCDIS):
        print("Triangle ABC is Equilatrial Equilangular")

    elif int(ABDIS) == int(ACDIS):
        print("Triangle ABC is Iscoloses")

    elif int(ABDIS) == int(BCDIS) :
        print("Triangle ABC is Iscoloses")

    elif int(ACDIS) == int(BCDIS) :
        print("Triangle ABC is Iscoloses")
    else:
        print("Triangle ABC is Scalene")
    

    print(" ")
#print("Points for reference")
#print("Point D = (" + str(DX) + "," + str(DY) + ")")
#print("Point E = (" + str(EX) + "," + str(EY) + ")")
#print("Point F = (" + str(FX) + "," + str(FY) + ")")
