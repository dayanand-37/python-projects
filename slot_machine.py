MAX_LINES = 3


def deposit():
    while True:
        amount = input("Enter the amount you want to deposit $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a valid amount.")
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


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()
