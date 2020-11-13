import math
print("This was created by Brady Van Oss you may download others like it at https://github.com/dawaffleman123/Math-Tools")
print("Welcome to the Animal Population Calculator!")
print("Start with a starting population ie lions and the calculator will do the rest")
i = 0
#Collect the Info
StartingPop = int(input("What is your starting population? "))
Multi = float(input("What would you like the populations to be multiplied as? "))
FMulti = Multi * 100
# Start the calculations
while i < 10:
    i = i + 1
    Pop = i * FMulti * FMulti
    print("Animal Level: " + str(i) + "  Population: " + str(Pop))
