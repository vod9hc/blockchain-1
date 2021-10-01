def game_quiz():
    score = 0
    player = input("Enter your name: ")
    print(player)

    Start = input("Do you play game?")
    if Start.lower() == "yes":
        print("Ok! Let's go")
    else:
        exit()
    quiz1 = input("CPU stands for: ")
    if quiz1.lower() == "center":
        score += 1
    else:
        print("Incorrect")

    quiz2 = input("GPU stands for: ")
    if quiz2.lower() == "right":
        print(quiz2)
        score += 1
    else:
        print("Incorrect")

    print(f"Your score: {score}")


def main():
    game_quiz()

if __name__ == '__main__':
    main()

