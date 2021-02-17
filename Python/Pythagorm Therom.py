import math
import colorama as cr
print("This was created by Brady Van Oss you may download others like it at "
      "https://github.com/dawaffleman123/Math-Tools")
print("Welcome to the Pythagorean Theorem Calculator!")
while True:
    Side = input("What side would you like to solve for(a, b, c)? ")

    if Side == "c":
        side_a = int(input("Side A >>> "))
        side_b = int(input("Side B >>> "))

        side_c = math.sqrt(side_a * side_a + side_b * side_b)

        print("Side C is equal to " + cr.Fore.GREEN + str(side_c))
        print(cr.Style.RESET_ALL)
    elif Side =="b":
        side_a = int(input('Side A >>> '))
        side_c = int(input('Side C >>> '))

        side_b = math.sqrt(side_c * side_c - side_a * side_a)

        print("Side B is equal to " + cr.Fore.GREEN + side_b)
        print(cr.Style.RESET_ALL)
    elif Side == "a":
        side_b = int(input('Side B >>> '))
        side_c = int(input('Side C >>> '))

        side_a = math.sqrt(side_c * side_c - side_b * side_b)

        print("Side B is equal to " + cr.Fore.GREEN + side_a)
        print(cr.Style.RESET_ALL)
    else:
        print(cr.Fore.RED + "Please chose either A, B, C" + cr.Style.RESET_ALL)
