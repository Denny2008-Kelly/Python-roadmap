import random       #This module allows random selection

choices = ["rock", "paper", "scissors",]

while True:         #This repeats the loop till the user stops
    for choice in choices:
        print(f"{choice}")
    
    print("Enter q to quit")        
    user_choice = input("Enter your choice: ").lower()
    
    if user_choice == "q":
        break

    if user_choice not in choices:
        print("Invaild choice")
        continue
        
    com_choice = random.choice(choices)
    print(f"My choice is {com_choice}")
    
    if com_choice == user_choice:
        print("It's a draw")
        
    elif((com_choice== "rock" and user_choice == "paper") or (com_choice == "paper" and user_choice == "scissors") or (com_choice == "scissors" and user_choice == "rock")):
        print("You win")
        
        
    else:
        print("You lose")
    
print("Thank you for playing this game")