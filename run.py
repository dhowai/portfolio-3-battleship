from random import randrange
import random


def check_position(boat, taken):

    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break
        elif num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat)-1:
            if boat[i+1] % 10 == 0:
                boat = [-1]
                break

    return boat


def check_boat(b, start, dirn, taken):

    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
            boat = check_position(boat, taken)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
            boat = check_position(boat, taken)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
            boat = check_position(boat, taken)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
            boat = check_position(boat, taken)

    return boat


def create_boats():
    taken = []
    ships = []
    boats = [5, 4, 3, 2, 2]
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            boat = check_boat(b, boat_start, boat_direction, taken)
        ships.append(boat)
        taken = taken + boat
        print(ships)

    return ships, taken


def show_board_comp(taken):
    """
    Function that shows the board when the game is run that the computer
    generates
    """
    print("             Battleships        \n")
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in taken:
                ch = " x "
            row = row + ch
            place = place + 1
        print(x, " ", row)


def get_shot_comp(guesses, tactics):

    ok = "n"
    while ok == "n":
        try:
            if len(tactics) > 0:
                shot = tactics[0]
            else:
                shot = randrange(99)
            if shot not in guesses:
                ok = "y"
                guesses.append(shot)
                break
        except ValueError:
            print("Incorrect entry please try again")

    return shot, guesses


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


def check_shot(shot, ships, hit, miss, done):

    missed = 0
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
                print("Hit")
            else:
                done.append(shot)
                missed = 2
                print("You Sunk My Battleship")
    if missed == 0:
        miss.append(shot)
        print("Miss")

    return ships, hit, miss, done, missed


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


def calc_tactics(shot, tactics, guessess, hit):

    temp = []
    if len(tactics) < 1:
        temp = [shot-1, shot+1, shot-10, shot+10]
    else:
        if shot-1 in hit:
            if shot-2 in hit:
                temp = [shot-3, shot+1]
            else:
                temp = [shot-2, shot+1]
        elif shot+1 in hit:
            if shot-2 in hit:
                temp = [shot+3, shot-1]
            else:
                temp = [shot+2, shot-1]
        elif shot-10 in hit:
            if shot-2 in hit:
                temp = [shot-30, shot+10]
            else:
                temp = [shot-20, shot+10]
        elif shot+10 in hit:
            if shot-2 in hit:
                temp = [shot+30, shot-10]
            else:
                temp = [shot+20, shot-10]

    cand = []
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])
    random.shuffle(cand)

    return cand


def check_if_empty_2(list_of_lists):
    return all([not elem for elem in list_of_lists])


hit = []
miss = []
done = []
guesses = []
ships, taken = create_boats()
tactics = []

for i in range(80):
    shot, guesses = get_shot_comp(guesses, tactics)
    ships, hit, miss, done, missed = check_shot(shot, ships, hit, miss, done)
    show_board(hit, miss, done)
    if missed == 1:
        tactics = calc_tactics(shot, tactics, guesses, hit)
    elif missed == 2:
        tactics = []
    elif len(tactics) > 0:
        tactics.pop(0)

    if check_if_empty_2(ships):
        print("end of game", i)
        break

show_board_comp(taken)
show_board(hit, miss, done)