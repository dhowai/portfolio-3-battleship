def get_shot(guesses):

    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("incorrect number, please try again")
            elif shot in guesses:
                print("Number already been guessed, try another")
            else:
                ok = "y"
                break
        except ValueError:
            print("Incorrect entry please try again")

    return shot


def show_board(hit, miss, done):
    """
    Function that shows the board when the game is run
    """
    print("             Battleships        \n")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " o "
            elif place in hit:
                ch = " x "
            elif place in done:
                ch = " X "
            
            row = row + ch
            place = place + 1
        print(x, " ", row)


hit = []
miss = []
done = []

guesses = hit + miss + done
shot = get_shot(guesses)
show_board(hit, miss, done)