def deposit():
    while True:
        amount = input("Enter the amount you want to deposit $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter the amount greater than 0.")
        else:
            print("Enter a valid amount.")

    return amount


def main():
    balance = deposit()

main()
