import random
import sys

def game():
    # Place car behind one door
    car = random.randint(1, 3)
    # Player selects a door
    first_choice = random.randint(1, 3)

    reveal_options = [1, 2, 3]
    # Don't reveal the car
    reveal_options.remove(car)
    # Don't reveal the player's choice
    if first_choice in reveal_options: reveal_options.remove(first_choice)
    # Reveal a door with a goat
    reveal = random.choice(reveal_options)

    second_options = [1, 2, 3]
    # Don't select your first choice
    second_options.remove(first_choice)
    # Don't select the revealed door
    second_options.remove(reveal)
    # Choose the remaining door
    second_choice = second_options[0]

    # Collect and return result
    first_succ = 1 if first_choice == car else 0
    second_succ = 1 if second_choice == car else 0
    return (first_succ, second_succ)

def simulate(rounds):
    first, second = 0, 0
    for i in range(rounds):
        res = game()
        first += res[0]
        second += res[1]
    print("First choice wins  {:.1f}% of cases".format(first / rounds * 100))
    print("Second choice wins {:.1f}% of cases".format(second / rounds * 100))

if __name__ == '__main__':
    simulate(int(sys.argv[1]))
