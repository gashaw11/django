
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
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.total_rounds = 0
        self.rps = ["rock", "paper", "scissors"]

    def get_user_move(self):
        user = input("Enter rock, paper, scissors or q to quit: ").lower()
        if user == "q":
            exit("Game exited by user.")
        if user not in self.rps:
            print("Invalid move")
            return None
        return user

    def get_computer_move(self):
        return random.choice(self.rps)

    def decide_winner(self, user, computer):
        if user == computer:
            return "Draw"
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            return "User"
        else:
            return "Computer"

    def get_final_result(self):
        if self.user_wins > self.computer_wins:
            return "User is the overall winner!"
        elif self.computer_wins > self.user_wins:
            return "Computer is the overall winner!"
        else:
            return "It's a tie overall!"

    def play(self):
        while self.total_rounds < 6:
            user_move = self.get_user_move()
            if user_move is None:
                continue

            computer_move = self.get_computer_move()
            print(f"Computer chose: {computer_move}")

            result = self.decide_winner(user_move, computer_move)

            if result == "User":
                self.user_wins += 1
                print("You won this round!")
            elif result == "Computer":
                self.computer_wins += 1
                print("Computer won this round!")
            else:
                print("This round is a draw!")

            self.total_rounds += 1
            print(f"Score: You {self.user_wins} - Computer {self.computer_wins}\n")

        print("--- Final Result ---")
        print(f"Final Score: You {self.user_wins} - Computer {self.computer_wins}")
        print(self.get_final_result())

# Create a game object and play
game = RockPaperScissorsGame()
game.play()
