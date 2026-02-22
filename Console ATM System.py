balance = 1000 # Initial balance

while True:
    print("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit") # Prints the options 
    
    
    try:
        option = int(input("Reply: "))      # User inputs prefared option
    except:
        print("Enter a valid number.")
        continue
    
    if option == 1:         # diplays balance
        print(f"Your balance is {balance}$")
    
    elif option == 2:       # Withdraws money
        try:
            w_amount = int(input("Enter amount to withdraw: \n"))
        except:
            print("Enter a valid number.")
            continue
        if w_amount < 0:
            print("Invalid input.Verify input")
        elif w_amount > balance :
            print("Invalid input.Verify input")
        else:
            balance -= w_amount
            print(f"Your current balance is {balance}$")
        
            
    
    elif option == 3:       # Deposits money
        try:
            d_amount = int(input("Enter amount to be deposited: \n"))
        except:
            print("Enter a valid number.")
            continue
        if d_amount > 0:
            balance += d_amount
            print(f"Your current balance is {balance}$")
        else:
            print("Invalid input.Verify input")
    
    elif option == 4:       # Quit
        break
    
    else:       # Prompts the user to do the right thing
        print(f"Enter a number from 1-4")
print("Thank you for using our ATM")
