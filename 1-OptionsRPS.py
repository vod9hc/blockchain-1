import random

def guess_number():
    user_wins = 0
    com_wins = 0
    options = ["rock", "paper", "scissor"]

    while True:
        random_options = random.randint(0, 2)
        com_options = options[random_options]

        print(" 0: Rock\n 1: Paper\n 2: Scissor")
        user_options = input("Please choose a your options or Type Q is quit: ").lower()
        if user_options == "q":
            break
        if user_options not in options:
            print("Please choose a correct options in next time.")
            continue
        print("Computer picked ", com_options)
        if user_options == "rock" and com_options == "scissor":
            print("You won.")
            user_wins += 1
        elif user_options == "scissor" and com_options == "paper":
            print("You won.")
            user_wins += 1
        elif user_options == "paper" and com_options == "rock":
            print("You won.")
            user_wins += 1
        else:
            print("Computer won.")
            com_wins += 1

    print("You won", user_wins, "times.")
    print("Computer won", com_wins, "times.")
    print("Good bye!")

def main():
    guess_number()

if __name__ == '__main__':
    main()