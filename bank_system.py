def valid(password):
    return len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password)

def signup(user_accounts, log_in, username, password):
    if username in user_accounts:
        return False
    if not valid(password):
        return False
    user_accounts[username] = password
    log_in[username] = False
    return True

def login(user_accounts, log_in, username, password):
    if username not in user_accounts:
        return False
    if not password == user_accounts[username]:
        return False
    log_in[username] = True
    return True

def logout(log_in, username):
    if username not in log_in or not log_in[username]:
        return False
    log_in[username] = False
    return True

def change_password(user_accounts, log_in, username, old_password, new_password):
    if username not in user_accounts or username not in log_in or not log_in[username]:
        return False
    if not user_accounts[username] == old_password:
        return False
    if not user_accounts[username] == new_password:
        if valid(new_password):
            user_accounts[username] = new_password
            return True
    return False

def update(bank, log_in, username, amount):
    if username in log_in and log_in[username]:
        if username in bank:
            val = bank[username] + amount
            if val >= 0:
                bank[username] = val
                return True
            return False
        else:
            if amount >= 0:
                bank[username] = amount
                return True
            return False
    return False

def delete_account(user_accounts, log_in, bank, username, password):
    if username not in user_accounts or username not in log_in or not log_in[username]:
        return False
    if user_accounts[username] != password:
        return False
    del user_accounts[username]
    del log_in[username]
    del bank[username]
    return True

def import_and_create_accounts(filename):
    user_accounts = {}
    try:
        with open(filename) as file:
            for line in file:
                if line.strip():
                    username, password = line.strip().split(',')
                    user_accounts[username] = password
    except FileNotFoundError:
        pass
    return user_accounts

def import_and_create_bank(filename):
    bank = {}
    try:
        with open(filename) as file:
            for line in file:
                if line.strip():
                    username, balance = line.strip().split(',')
                    bank[username] = float(balance)
    except FileNotFoundError:
        pass
    return bank

def import_and_create_logins(filename):
    log_in = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                username, status = line.strip().split(',')
                log_in[username] = status == "True"
    except FileNotFoundError:
        pass
    return log_in

def save_accounts(user_accounts, filename="accounts.txt"):
    with open(filename, "w") as file:
        for username, password in user_accounts.items():
            file.write(f"{username},{password}\n")

def save_bank(bank, filename="bank.txt"):
    with open(filename, "w") as file:
        for username, balance in bank.items():
            file.write(f"{username},{balance}\n")

def save_logins(log_in, filename):
    with open(filename, 'w') as f:
        for username, status in log_in.items():
            f.write(f"{username},{status}\n")

