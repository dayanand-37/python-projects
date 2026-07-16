MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("Enter the amount you want to deposit $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter a Number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the lines you want to bet between (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter lines between the given range.")
        else:
            print("Enter a number.")

    return lines


def get_bet():
    while True:
        amount = input(
            f"Enter the amount you want to bet on each line between ${MIN_BET} - ${MAX_BET}: "
        )
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Enter the amount between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a number.")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You do not have enough balance, your current balance is ${balance} "
            )
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines and your total bet amount is ${total_bet}"
    )


main()