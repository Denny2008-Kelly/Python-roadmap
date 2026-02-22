import random       #This module allows random selection

choices = ["rock", "paper", "scissors",]

while True:         #This repeats the loop till the user stops
    for choice in choices:
        print(f"{choice}")
    
    print("Enter q to quit")        
    user_choice = input("Enter your choice: ").lower()
    
    if user_choice == choices[0]:       # This blocks is for when user enters "rock"
        com_choice = random.choice(choices)
        print(f"My choice is {com_choice}")
        
        if com_choice == 'rock':
            print("It's a draw")
        
        elif com_choice == 'paper':
            print("You lose")

        elif com_choice == 'scissors':
            print("You win")

    elif user_choice == choices[1]:         # This blocks is for when user enters "paper"
        com_choice = random.choice(choices)
        print(f"My choice is {com_choice}")
        
        if com_choice == 'rock':
            print("You win")
        
        elif com_choice == 'paper':
            print("It's a draw")

        elif com_choice == 'scissors':
            print("You lose")

    elif user_choice == choices[2]:         # This blocks is for when user enters "scissors"
        com_choice = random.choice(choices)
        print(f"My choice is {com_choice}")
        
        if com_choice == 'rock':
            print("You lose")
        
        elif com_choice == 'paper':
            print("You win")

        elif com_choice == 'scissors':
            print("It's a draw")
    
    elif user_choice == 'q':        # This blocks is for when user enters wants to quit
        print("Thanks for playing this game")
        break
    
    else:           # Ensures the code doesn't crash from wrong input
        print("Enter a valid choice")