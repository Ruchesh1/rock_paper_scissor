import random
import string


oppenent_choices = ["ROCK", "PAPER", "SCISSOR"]

user = " "

while True:
    oppenent = random.choice(oppenent_choices)
    user = input("Pick either Rock, Paper or Scissor: ").upper()
    if user == oppenent_choices[0] or user == oppenent_choices[1] or user == oppenent_choices[2]:
        if user == oppenent:
            print(f"Tie your choice: {user} vs oppenent choice: {oppenent}, Try Again")
        else:
            print(f"your choice: {user} vs oppenent choice: {oppenent}")
            break
    else:
        print("Invalid Choice Try Again")


    

        





