import math

print("This was created by Brady Van Oss you may download others like it at "
      "https://github.com/dawaffleman123/Math-Tools")
print("Welcome to the Pythagorean Theorem Calculator!")

while True:
    opp = ""
    type = ""
    gram = ""
    while True:
        num1 = float(input("What is the first number? "))
        num2 = float(input("What is the second number? "))
        num3 = float(input("What is the third number? "))

        numarr = [num1, num2, num3]
        print(f"The largest number is {max(numarr)}")

        smallnums = num1 + num2 + num3 - max(numarr)

        if smallnums > max(numarr):
            print(f"{smallnums} > {max(numarr)}")
        else:
            print("These numbers do not make a triangle")
            print(f"{smallnums} />/ {max(numarr)}")
            break

        num1py = num1 * num1
        num2py = num2 * num2
        num3py = num3 * num3
        smallSidePy = num1py + num2py
        if smallSidePy == num3py:
            opp = "="
            type = "Right"
            gram = "a"
        elif smallSidePy < num3py:
            opp = "<"
            type = "Obtuse"
            gram = "an"
        elif smallSidePy > num3py:
            opp = ">"
            type = "Accute"
            gram = "an"
        else:
            print("Welp the impossible just happened crap well here you go")
            break

        print()
        print(f"{num1}^2 + {num2}^2 = {num3}^2")
        print(f"{num1py} + {num2py} = {smallSidePy}")
        print(f"{smallSidePy} {opp} {num3py}")
        print(f"This is {gram} {type} triangle")
        print()


