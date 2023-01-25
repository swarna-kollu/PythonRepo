import sys
from sys import argv
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")


num1 = int(argv[1])
print(num1)
num2 = int(argv[2])
print(num2)
select = int(input("Select operations form 1, 2, 3, 4 :"))
if select == 1:
    print(num1, "+", num2, "=",num1+num2)
elif select == 2:
    print(num1, "-", num2, "=",num1-num2)
elif select == 3:
    print(num1, "*", num2, "=",num1*num2)
elif select == 4:
    print(num1, "/", num2, "=",num1/num2)
else:
    print("Invalid input")


