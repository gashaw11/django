
#this is rock, paper,and scissors game


#list
#module
#user choice which is an input
#game rule
#decide the whowins
user_wins = 0
computer_wins = 0
total_rounds = 0
import random

rps = ["paper","rock","scissors"]
  
    
while total_rounds <6:
    total_rounds +=1
    computer_move = random.choice(rps)   
    user = input("enter rock,paper,scissors ").lower()
    if user not in rps:
        print("invalid")
        continue

    if computer_move == user:
        print("draw")
    elif computer_move == "paper" and user == "rock":
        print("computer won")
        computer_wins +=1 
    elif computer_move == "scissors" and user == "paper":
        print("computer won")
        computer_wins +=1 
    elif computer_move == "rock" and user == "scissors":
        print("computer won") 
        computer_wins +=1
    else:
        print("user won") 
        user_wins +=1
if user_wins > computer_wins:
    print("User is the overall winner!")
elif computer_wins > user_wins:
    print("Computer is the overall winner!")
else:
    print("It's a tie overall!")

