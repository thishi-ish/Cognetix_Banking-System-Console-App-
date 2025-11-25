import json
import os

ACCOUNT_FILE = "account_data.json"


def load_balance():
    """Load balance from file or create one if missing."""
    if not os.path.exists(ACCOUNT_FILE):
        data = {"balance": 0}
        with open(ACCOUNT_FILE, "w") as f:
            json.dump(data, f)
        return 0

    with open(ACCOUNT_FILE, "r") as f:
        data = json.load(f)
        return data.get("balance", 0)


def save_balance(balance):
    """Save updated balance to file."""
    with open(ACCOUNT_FILE, "w") as f:
        json.dump({"balance": balance}, f)


def deposit(amount):
    balance = load_balance()
    balance += amount
    save_balance(balance)
    print(f"✔ Successfully deposited ₹{amount}. New Balance: ₹{balance}")


def withdraw(amount):
    balance = load_balance()
    if amount > balance:
        print("❌ Withdrawal failed! Insufficient balance.")
    else:
        balance -= amount
        save_balance(balance)
        print(f"✔ Successfully withdrew ₹{amount}. Remaining Balance: ₹{balance}")


def check_balance():
    balance = load_balance()
    print(f"💰 Current Balance: ₹{balance}")


def main():
    print("\n===== SIMPLE BANKING SYSTEM =====")
    
    while True:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            amount = int(input("Enter amount to deposit: "))
            deposit(amount)

        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            withdraw(amount)

        elif choice == "3":
            check_balance()

        elif choice == "4":
            print("👋 Exiting... Thank you for using the banking system.")
            break

        else:
            print("⚠ Invalid choice. Try again!")


if __name__ == "__main__":
    main()
