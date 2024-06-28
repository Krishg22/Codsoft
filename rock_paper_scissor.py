#snake water game
import random
chc=["snake","water","gun"]
# com_choice=random.choice(chc)
print("welcome to sanke water game")
score_user = 0
score_computer = 0
while(True):
    user_choice = input("Enter your choice(snake, water, gun) or quit :")
    user_choice = user_choice.lower()
    com_choice=random.choice(chc)
    if(user_choice.lower() == "quit"):
        break
    if(user_choice=="snake" and com_choice=="snake"):
        print("your choice:",user_choice)
        print("computer choice:",com_choice)
        print("Tie")
        score_user += 1
        score_computer += 1
    elif(user_choice=="snake" and com_choice=="water"):
        print("your choice:",user_choice)
        print("computer choice:",com_choice)
        print("you won")
        score_user += 1
    elif(user_choice=="snake" and com_choice=="gun"):
        print("your choice:",user_choice)
        print("computer choice:",com_choice)
        print("you loss")
        score_computer += 1
    elif(user_choice=="water" and com_choice=="snake"):
        print("your choice:",user_choice)
        print("computer choice:",com_choice)
        print("you loss")
        score_computer += 1
    elif(user_choice=="water" and com_choice=="water"):
        print("your choice:",user_choice)
        print("computer choice:",com_choice)
        print("Tie")
        score_user += 1
        score_computer += 1
    elif(user_choice=="water" and com_choice=="gun"):
        print("your choice:",user_choice)
        print("computer choice:",com_choice)
        print("you won")
        score_user += 1
    elif(user_choice=="gun" and com_choice=="snake"):
        print("your choice:",user_choice)
        print("computer choice:",com_choice)
        print("you won")
        score_user += 1
    elif(user_choice=="gun" and com_choice=="water"):
        print("your choice:",user_choice)
        print("computer choice:",com_choice)
        print("you loss")
        score_computer += 1
    elif(user_choice=="gun" and com_choice=="gun"):
        print("your choice:",user_choice)
        print("computer choice:",com_choice)
        print("Tie")
        score_computer += 1
        score_user += 1

print("--Game over--")
print("Your score:",score_user)
print("Computer score:",score_computer)