#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

abs_num = abs(number)
num2 = abs_num % 1000
num3 = num2 % 100
num4 = (num3 % 10)

if num4 > 5:
    if number * -1 == abs_num:
        num4 = num4 * -1
        print("Last digit of %d" %number + " is %d " %num4
            +"and is greater than 5")

elif num4 < 6 and num4 > 0:
    if number * -1 == abs_num:
        num4 = num4 * -1
        print("Last digit of %d" %number + " is %d " %num4
             + "and is less than 6 and not 0")

else:
    if number * -1 == abs_num:
        num4 = num4 * -1
        print("Last digit of %d" %number + " is %d " %num4 +
            "and is 0")
