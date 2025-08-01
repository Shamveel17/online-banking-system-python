from bank_system import *

def cli():
    
    user_accounts = import_and_create_accounts("accounts.txt")
    log_in = import_and_create_logins("logins.txt")
    bank = import_and_create_bank("bank.txt")
    
    while True:
        print("\n--- Simple CLI Bank ---")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Log Out")
        print("4. Change Password")
        print("5. Update Account Balance")
        print("6. Delete Account")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if signup(user_accounts, log_in, username, password):
                save_accounts(user_accounts)
                save_logins(log_in, "logins.txt")
                print("Sign up successful.")
            else:
                print("Sign up failed. Username may already exist or password is invalid.")
                print("Password must be at least 8 characters long and include:")
                print("- At least one uppercase letter")
                print("- At least one lowercase letter")
                print("- At least one digit")


        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(user_accounts, log_in, username, password):
                save_logins(log_in, "logins.txt")
                print("Login successful.")
            else:
                print("Login failed.")

        elif choice == '3':
            username = input("Enter username: ")
            if logout(log_in, username):
                save_logins(log_in, "logins.txt") 
                print("Logout successful.")
            else:
                print("Logout failed.")

        elif choice == '4':
            username = input("Enter username: ")
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            if change_password(user_accounts, log_in, username, old_password, new_password):
                save_accounts(user_accounts)
                print("Password changed successfully.")
            else:
                print("Password change failed.")

        elif choice == '5':
            username = input("Enter username: ")
            amount = float(input("Enter amount (+/-): "))
            if update(bank, log_in, username, amount):
                save_bank(bank)
                print(f"Balance updated. New balance: {bank[username]:.2f}")
            else:
                print("Balance update failed.")

        elif choice == '6':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if delete_account(user_accounts, log_in, bank, username, password):
                save_accounts(user_accounts)
                save_bank(bank)
                save_logins(log_in, "logins.txt")
                print("Account deleted successfully.")
                print("Note:Account deletion would be if user is logged in.")
            else:
                print("Account deletion failed.")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == '__main__':
    user_accounts = import_and_create_accounts("accounts.txt")
    log_in = {}
    bank = import_and_create_bank("bank.txt")
    cli()
