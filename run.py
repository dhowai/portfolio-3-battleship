from random import randrange


def check_position(boat):

    for i in range(len(boat)):
        num = boat[i]
        if num < 0 or num > 99:
            boat = [-1]
            break

    return boat


def check_boat(b, start, dirn):

    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_position(boat)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
            boat = check_position(boat)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
            boat = check_position(boat)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
            boat = check_position(boat)
    print(boat)


boats = [5]
for b in boats:
    boat_start = randrange(99)
    boat_direction = randrange(1, 4)
    check_boat(b, boat_start, boat_direction)


def get_shot(guesses):

    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess:")
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


def check_shot(shot, boat1, hit, miss, done):

    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
            print("Hit")
        else:
            done.append(shot)
            print("You Sunk My Battleship")
    else:
        miss.append(shot)
        print("Miss")

    return boat1, hit, miss, done


boat1 = [45, 46, 47]
hit = []
miss = []
done = []

for i in range(10):
    guesses = hit + miss + done
    shot = get_shot(guesses)
    boat1, hit, miss, done = check_shot(shot, boat1, hit, miss, done)
    show_board(hit, miss, done)

    if len(boat1) < 1:
        print("You Won!")
        break
print("Finished")