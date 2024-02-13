#TerryPaul hd9796 2/13/24 Game OF chance
#begin
import random

# Withdraw and validate function
def withdraw_and_validate(acc, wager_amount):
    if Bank[acc] >= wager_amount:
       #per sonfication and visulzation requirment
        print("Doing the calculations for withdrawals")
        print(f"{Bank[acc]} - {wager_amount}")
        Bank[acc] -= wager_amount
        print("Placing your wager of", wager_amount)
        return True
    else:
        print("Not enough money, please enter another wager.")
        return False

# Function to select a specified number of random items from Items
def select_random_items(n):
    if n > len(Items):
        print("Request exceeds available items, selecting all items instead.")
        return list(Items.keys())
    else:
        return random.sample(list(Items.keys()), n)

# Initializing bank accounts with random balances
Items = {'gun': 50, 'toy': 5, 'book': 20, 'pen': 3, 'ball': 15, 'laptop': 500, 'phone': 300, 'chair': 25, 'desk': 100, 'cup': 8}
Bank = {"Account1": 0, "Account2": 0, "Account3": 0}

# Initializing the balances of accounts
for account in Bank:
    Start_Bal = random.randint(500, 1000)
    Bank[account] = Start_Bal
    print(account, "has a balance of", Start_Bal)

# Game loop
while Bank['Account1'] > 0:
    print("\nYou are playing against 3 other players. Once your account balance is 0, the game is over.")
    # Ask user for the number of items they'd like to play with
    num_items = int(input("How many items would you like to play with? "))
    wager_items = select_random_items(num_items)
    print("Selected items for this round:", wager_items)

    for random_key in wager_items:
        print("Wagering for item:", random_key, "with the price of", Items[random_key])
        
        participants = random.randint(1, 2)  # Number of other participants
        print(participants, "other(s) want this item")
        other_wagers = [random.randint(1, Bank[f"Account{i+2}"]) for i in range(participants)]  # Random wagers by other accounts
        
        wager = int(input("Enter your wager amount: "))
        if not withdraw_and_validate("Account1", wager):
            continue  # Skip the rest of this iteration if wager is not valid
        
        # Determine the winner based on the highest wager
        highest_wager = max(wager, max(other_wagers))
        if highest_wager == wager:
            print("Congratulations! You won the item:", random_key)
        else:
            print("You lost this round. The highest wager was", highest_wager)

        print("Your current balance:", Bank['Account1'])
        
        if Bank['Account1'] <= 0:
            print("Your bank account has been plundered to the depths! Game over.")
            break

    if Bank['Account1'] > 0 and input("Play again? (yes/no): ").lower() != "yes":
        print("You ended your pirate adventure with a balance of", Bank['Account1'], "gold coins. Farewell!")
        break
#end
