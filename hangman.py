def hangman(word):
    wrong = 0
    stages = (
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              )
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman\n")
    print("Take a moment to gaze at your word\n")

    for space in board:
            print(space, end=" ")

    while wrong < len(stages):
        letter = input("\n\nGuess an alphabet: ")

        if letter in word:
            print("Nice, you guessed right")
            indices = [i for i, x in enumerate(rletters) if x == letter]
            for indexRunner in indices:
                board[indexRunner] = rletters[indexRunner]

            for space in board:
                print(space, end=" ")

            if board == rletters:
                return True

        else:
            print("Aww man, wrong move\n")
            wrong += 1
            for iterator in range(0, wrong):
                print(stages[iterator])
            print("\nYou have ", len(stages) - wrong, "more chance(s) to fuck up")

    return False
    
word = "panorama"

if hangman(word):
    print("\n\nNot bad, it seems that you have succeeded")
else:
    print("\nYou are a pathetic failure")