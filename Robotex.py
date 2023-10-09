import random
from colorama import init, Fore, Style

init(autoreset=True)


def generate_pin():
    return [random.randint(0, 9) for _ in range(4)]


def check_pin(user_pin, correct_pin):
    result = []
    for i in range(4):
        if user_pin[i] == correct_pin[i]:
            result.append(Fore.GREEN + "Correct!")
        elif user_pin[i] in correct_pin:
            result.append(Fore.YELLOW + "Wrong Spot.")
        else:
            result.append(Fore.RED + "Incorrect!")
    return result


max_attempts = 5


def main():
    while True:
        correct_pin = generate_pin()

        print(Fore.GREEN + "Welcome to the Box PIN Game!")
        print("You have {} attempts.".format(max_attempts))
        print(Style.RESET_ALL)

        for attempt in range(1, max_attempts + 1):
            print("\n" + Fore.CYAN + "Attempt #{}".format(attempt))
            user_input = input("Enter a 4-digit PIN: ")

            if len(user_input) != 4 or not user_input.isdigit():
                print(Fore.RED + "Invalid input! Please enter a 4-digit PIN.")
                continue

            user_pin = [int(digit) for digit in user_input]

            result = check_pin(user_pin, correct_pin)
            print("Result: ", " ".join(result))

            if result == [Fore.GREEN + "Correct!"] * 4:
                print(Fore.GREEN + "Congratulations! You entered the correct PIN.")
                break

            if attempt < max_attempts:
                print(Fore.YELLOW + "Try again.")

        if result != [Fore.GREEN + "Correct"] * 4:
            print(Fore.RED + "Sorry, you've used all your attempts. The correct PIN was:", correct_pin)

        play_again = input(Fore.CYAN + "Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break


if __name__ == "__main__":
    main()
