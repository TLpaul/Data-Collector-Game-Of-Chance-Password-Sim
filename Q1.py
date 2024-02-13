#TerryPaul hd9796 2/13/24 Data Collector app
#begin
import random  # generate names

# dictionary to store data 
Data = {}

def Data_Collector(unique_id):
    names = ["User1", "User2", "User3", "User4", "User5", "User6", "User7", "User8", "User9", "User10"]
    Passwords = ['B+1H`Vuz-tQJ', 'dIuD+.<[vEr}', 'r;$F3w$h-)-<', 'r?2,dZ4k(7cY', '3lc#Qj#SR0.K', 'Rq6guN|"q72x', 'QF%b->vnbf.G', '-ev9O;XLJVCD', 'hZ9`kyfS~[ha', 'D&mI%axsly::']
    birthdates = ["01/01/1990", "02/02/1991", "03/03/1992", "04/04/1993", "05/05/1994", "06/06/1995", "07/07/1996", "08/08/1997", "09/09/1998", "10/10/1999"]
    addresses = ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St", "202 Birch St", "303 Cedar St", "404 Maple St", "505 Walnut St", "606 Cherry St", "707 Aspen St"]
    ssns = ["111-11-1111", "222-22-2222", "333-33-3333", "444-44-4444", "555-55-5555", "666-66-6666", "777-77-7777", "888-88-8888", "999-99-9999", "000-00-0000"]
    productsPurchased = ["ID-Laptop", "ID-Smartphone", "ID-Tablet", "ID-Headphones", "ID-Smartwatch", "ID-Book", "ID-Video Game", "ID-Backpack", "ID-Camera", "ID-Printer"]
    salespersons = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia"]
    
    random_index = random.randint(0, 9)
    #needs to be random index from each list 
    
    user_data = {
        "Username": names[random_index],
        "Password": Passwords[random_index],
        "Birthdate": birthdates[random_index],
        "Address": addresses[random_index],
        "SSN": ssns[random_index],
        "ProductPurchased": productsPurchased[random_index],
        "Salesperson": salespersons[random_index]
    }
    
    Data[str(unique_id)] = user_data
    print(f"Data collected for User ID {unique_id}: {user_data['Username']}")

def generate_unique_id():
    return len(Data) + 1

def search_data(username):
    found = False
    for user_id, user_info in Data.items():
        if user_info.get('Username') == username:
            print(f"User data found for Username '{username}': User ID {user_id}, User Info: {user_info}")
            found = True
    if not found:
        print(f"No data found for Username '{username}'.")

# Main program loop with menu
while True:
    print("\nMenu:")
    print("1 - Add new user")
    print("2 - Search data by Username")
    print("3 - Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        unique_id = generate_unique_id()
        Data_Collector(unique_id)
    elif choice == '2':
        username = input("Enter username to search: ")
        search_data(username)
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid option, please try again.")
 #end
