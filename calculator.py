print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
select = int(input("Select operations form 1, 2, 3, 4 :"))
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
if select == 1:
    print(num_1, "+", num_2, "=",num_1+num_2)
elif select == 2:
    print(num_1, "-", num_2, "=",num_2-num_2)
elif select == 3:
    print(num_1, "*", num_2, "=",num_1*num_2)
elif select == 4:
    print(num_1, "/", num_2, "=",num_1/num_2)
else:
    print("Invalid input")