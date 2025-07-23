# This is a simple Python script
def show_balance(balance):
    print(f"=> Your balance is ${balance:.2f}")
    print()
def deposit():
    amount = float(input("Enter an amount to be deposited: $"))
    if amount <0:
        print("=> Your amount cannot be negative!")
        print()
        return 0
    else:
        print("=> Your transaction has been successful!")
        print()
        return amount
def withdraw(balance):
    amount = float(input("Enter an amount to be withdraw: $"))
    if amount > balance:
        print("=> Insufficient funds")
        return 0
    elif amount <0:
        print("=> Your amount cannot be negative!")
        return 0
    else:
        print("=> Your transaction has been successful!")
        return amount

def main():
    balance = 0
    running = True
    while running:
        print("*******************")
        print("  Banking Program"  )
        print("*******************")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*******************")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        else:
            running = False
    print("****************************")
    print("Thank you! Have a great day!")
    print("****************************")


if __name__ == "__main__":
    main()