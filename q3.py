#Terry Paul hd9796 2/12/24 p3
#begin
import random

#TerryP 2/13/24 revison # 1
# Function to generate a single password
def genPass():
    Alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Symbols = ["!", "@", "#", "$"]
    Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    Password = []

    for _ in range(8):  # Ensure at least 8 characters
        LorS = random.randint(0, 1)
        
        if LorS == 0:  # Choose letter
            Let = random.choice(Alpha)
            UorL = random.randint(0, 1)  # Decide upper or lower case
            if UorL == 0:
                Password.append(Let.upper())
            else:
                Password.append(Let)
        else:  # Choose symbol or number
            SorN = random.randint(0, 1)
            if SorN == 0:
                Password.append(random.choice(Symbols))
            else:
                Password.append(str(random.choice(Numbers)))  # Convert number to string

#TerryP 2/13/24 revison # 2
    return ''.join(map(str, Password))

def validatePassword(password):
    #if all thes come bacvk true then return password
    has_symbol = False
    has_number = False
    has_uppercase = False
    
    # List of symbols for the check
    symbols = ["!", "@", "#", "$"]
    
    # Check each character in the password
    for char in password:
        if char in symbols:
            has_symbol = True
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_uppercase = True
            
    # all conditions are met
    return has_symbol and has_number and has_uppercase
# Main code to generate 40 valid passwords
valid_passwords = []


#TerryP 2/13/24 revison # 3
#per 40 iteration requirement 
while len(valid_passwords) < 40:
    new_password = genPass()
    if validatePassword(new_password):
        valid_passwords.append(new_password)

# Print the list of valid passwords
print(f"Generated {len(valid_passwords)} valid passwords:")
for password in valid_passwords:
    print(password)
 #end  