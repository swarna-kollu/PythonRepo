print("Memory Game")

"""first_player
second_player"""

print("Numbers only")
print()
print("first player")
x=0
level = True
while level == True and x<2:
    card1=input("card number1 :")
    print("take the card and turn it over")
    card2=input("card number2 :")
    if card1==card2:
        print("Cards matches and Awarded another turn")
        x+=1
    elif card1!=card2:
        while level == True and x<2:
            print("Cards did not match and next player turn")  
            card1=input("card number1 :")
            print("take the card and turn it over")
            card2=input("card number2 :")
            if card1==card2:
                # print("Cards matches and Awarded another turn")
                x+=1
            elif card1!=card2:
                print("cards did not match")    
                level=False
        

