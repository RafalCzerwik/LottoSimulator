import random


def get_numbers():
    """Get a single number from the player."""
    while True:
        try:
            number = int(input("Your number: "))
            if 1 <= number <= 49:
                return number
            else:
                print("Number must be in range 1-49!")
        except ValueError:
            print("It's not a number!")


def check_numbers():
    """Get 6 unique numbers from the player and return them sorted."""
    player_numbers = []
    while len(player_numbers) < 6:
        numbers = get_numbers()
        if numbers in player_numbers:
            print("You choose this number already! Try again!")
        else:
            player_numbers.append(numbers)
    return sorted(player_numbers)


def lotto():
    """Simulate a lotto draw and compare player's numbers with the drawn numbers."""
    print("Welcome in LOTTO Simulator!!!")
    print("You must choose 6 numbers!\n")
    lucky_numbers = check_numbers()
    lotto_results = []
    lotto_numbers = random.sample(range(1, 49), 6)
    sorted_lotto = sorted(lotto_numbers)
    for number in lucky_numbers:
        if number in sorted_lotto:
            lotto_results.append(number)
    hits = len(lotto_results)
    print(f"Your numbers: \n{lucky_numbers}\n")
    print(f"Lotto numbers: \n{sorted_lotto}\n")
    print(f"You have {hits} {'hit' if hits == 1 else 'hits'}!")


if __name__ == '__main__':
    lotto()
