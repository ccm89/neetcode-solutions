class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
alice_acct = BankAccount("Alice", 1000)
bob_acct = BankAccount("Bob", 2000)

# TODO: Print the information using the mentioned format
print(f"{alice_acct.name}'s balance: ${alice_acct.balance}")
print(f"{bob_acct.name}'s balance: ${bob_acct.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")