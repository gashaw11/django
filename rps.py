
#this is rock, paper,and scissors game


#list
#module
#user choice which is an input
#game rule
#decide the whowins
#get_user_move()
#get_get_computer_move()
#print_final_result()
#main()
user_wins = 0
computer_wins = 0
total_rounds = 0
import random

rps = ["paper","rock","scissors"]

def get_user_move():
    user = input("enter rock,paper,scissors or q for quit").lower()
    if user not in rps:
        print("invalid move")
        return None
    return user

def get_get_computer_move():
    return random.choice(rps)

def decide_winner(user,computer_move):
    global user_wins, computer_wins
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

def print_final_result():
    if user_wins > computer_wins:
        print("User is the overall winner!")
    elif computer_wins > user_wins:
        print("Computer is the overall winner!")
    else:
        print("It's a tie overall!")
    
    


def main():
    global total_rounds
    while total_rounds < 6:
        user_move = get_user_move()
        if user_move is None:
            continue
        get_computer_move = get_get_computer_move()
        decide_winner(user_move, get_computer_move)
        total_rounds += 1

    print_final_result()

main()