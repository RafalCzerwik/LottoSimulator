import random


def get_number():
    """Get number from user"""
    while True:
        try:
            number = int(input("Choose a number: "))
            if 1 <= number <= 49:
                return number
            else:
                print("Number must be in range 1-49!")
        except ValueError:
            print("It must be a number!")


def get_guesses():
    """Get number from user and save in list"""
    user_numbers = []
    while len(user_numbers) < 6:
        number = get_number()
        if number in user_numbers:
            print("You've already entered that number!")
        else:
            user_numbers.append(number)
    return sorted(user_numbers)


def lotto():
    """Main function with choose 6 random numbers"""
    print("Welcome to the LOTTO simulator!")
    user_numbers = get_guesses()
    print(f"Your number: {user_numbers}")

    lotto = sorted(random.sample(range(1, 50), 6))
    print(f"Drawn numbers: {lotto}")

    hits = len(set(user_numbers) & set(lotto))
    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == "__main__":
    lotto()
