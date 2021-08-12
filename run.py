from random import randrange
import random
from pyfiglet import Figlet


def check_position(boat, taken):
    """
    Function to keep user and computer input on their respective boards
    """
    boat.sort()
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
        if i != 0:
            if boat[i] != boat[i-1]+1 and boat[i] != boat[i-1]+10:
                boat = [-1]
                break

    return boat


def get_ship(long, taken):
    """
    Function for user to input their ship locations
    """
    ok = True
    while ok:
        try:
            ship = []
            print("Setting up board...")
            print("Enter your ship of length:", long)
            for _ in range(long):
                boat_num = input("Please enter a number:\n")
                ship.append(int(boat_num))
            ship = check_position(ship, taken)
            if ship[0] != -1:
                taken = taken + ship
                break
            else:
                print("""
            Error - number already used or
            ship was not in correct order, please try again
            """)
        except ValueError:
            print("Error - not a number, please try again")

    return ship, taken


def create_boats(taken, boats):
    """
    Function for user ships making sure no repeats of ships
    """
    ships = []

    for boat in boats:
        ship, taken = get_ship(boat, taken)
        ships.append(ship)

    return ships, taken


def check_boat(b, start, dirn, taken):
    """
    Function to keep boat directions vertical and horizontal
    """
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
    boat = check_position(boat, taken)

    return boat


def create_boats_comp(taken, boats):
    """
    Function creates computer ships at random in board dimentions
    """
    ships = []
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            boat = check_boat(b, boat_start, boat_direction, taken)
        ships.append(boat)
        taken = taken + boat

    return ships, taken


def show_board_p(taken):
    """
    Function that shows the players ship loactions
    """
    print("                       Player ships               \n")
    print("      0    1    2    3    4    5    6    7    8    9")

    place = 0
    for x in range(10):
        row = ""
        for _ in range(10):
            ch = " [ ] "
            if place in taken:
                ch = " [x] "
            row = row + ch
            place = place + 1
        print(x, " ", row)


def get_shot_comp(guesses, tactics):
    """
    Function that the computer uses to hit user ships
    """
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
    Function that shows the user's board
    """
    print("                       Battle               ")
    print("      0    1    2    3    4    5    6    7    8    9")

    place = 0
    for x in range(10):
        row = ""
        for _ in range(10):
            ch = " [ ] "
            if place in miss:
                ch = " [o] "
            elif place in hit:
                ch = " [x] "
            elif place in done:
                ch = " [X] "

            row = row + ch
            place = place + 1
        print(x, " ", row)


def check_shot(shot, ships, hit, miss, done):
    """
    Function that updates the respective lists depending on outcome
    """
    missed = 0
    for i in range(len(ships)):
        if shot in ships[i]:
            ships[i].remove(shot)
            if len(ships[i]) > 0:
                hit.append(shot)
                missed = 1
                custom_fig = Figlet(font='doom')
                print(custom_fig.renderText('Hit!'))
            else:
                done.append(shot)
                missed = 2
                custom_fig = Figlet(font='doom')
                print(custom_fig.renderText('Sunk a Battleship!'))
    if missed == 0:
        miss.append(shot)
        custom_fig = Figlet(font='doom')
        print(custom_fig.renderText('Miss'))

    return ships, hit, miss, done, missed


def calc_tactics(shot, tactics, guesses, hit):
    """
    Function that helps the computer make tactical guesses to where the user
    ships are
    """
    temp = []
    if len(tactics) < 1:
        temp = [shot-1, shot+1, shot-10, shot+10]
    else:
        if shot-1 in hit:
            temp = [shot+1]
            for i in [2, 3, 4, 5, 6, 7, 8]:
                if shot-i not in hit:
                    temp.append(shot-i)
                    break
        elif shot+1 in hit:
            temp = [shot-1]
            for i in [2, 3, 4, 5, 6, 7, 8]:
                if shot+i not in hit:
                    temp.append(shot+i)
                    break
        if shot-10 in hit:
            temp = [shot+10]
            for i in [20, 30, 40, 50, 60, 70, 80]:
                if shot-i not in hit:
                    temp.append(shot-i)
                    break
        elif shot+10 in hit:
            temp = [shot-10]
            for i in [20, 30, 40, 50, 60, 70, 80]:
                if shot+i not in hit:
                    temp.append(shot+i)
                    break

    cand = []
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])
    random.shuffle(cand)

    return cand


def get_shot(guesses):
    """
    Function that user enters guess and parameters if an error occurs
    """
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess:\n")
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


def check_if_empty_2(list_of_lists):
    return all([not elem for elem in list_of_lists])


# Before Game

menu = {}
menu['1:'] = "Play Game"
menu['2:'] = "About Game"
while True:
    options = menu.keys()
    custom_fig = Figlet(font='doom')
    print(custom_fig.renderText('Welcome \nto Battleship'))
    for entry in options:
        print(entry, menu[entry])

    selection = input("Please Select:\n")
    if selection == '2':
        print("""
        This is a game of Battleship made in python.
        The user plays against the computer,
        each will place ship locations on their 0-99 board and
        the other has to guess where they are.
        The player that destroys the others ships first
        is then declared the winner.
        """)
    elif selection == '1':
        break
    else:
        print("Unknown Option Selected")


# Board 1
hit1 = []
miss1 = []
done1 = []
guesses1 = []
missed1 = 0
tactics1 = []
taken1 = []

# Board 2
hit2 = []
miss2 = []
done2 = []
guesses2 = []
missed2 = 0
tactics2 = []
taken2 = []

battleships = [5, 4, 3, 2]
# Computer
ships1, taken1 = create_boats_comp(taken1, battleships)

# User
ships2, taken2 = create_boats(taken2, battleships)
show_board_p(taken2)

# Game loop
for i in range(100):
    """
    Function that contains the game loop of user and computer
    """
# Player shoots

    print("Player")
    guesses1 = hit1 + miss1 + done1
    shot1 = get_shot(guesses1)
    ships1, hit1, miss1, done1, missed1 = check_shot(shot1, ships1, hit1, miss1, done1)
    show_board(hit1, miss1, done1)
# repeats till ships are empty
    if check_if_empty_2(ships1):
        print("\nEnd of game - Player Wins in", i)
        show_board(hit2, miss2, done2)
        break

# Computer shoots until ships are empty

    print("Computer")
    shot2, guesses2 = get_shot_comp(guesses2, tactics2)
    ships2, hit2, miss2, done2, missed2 = check_shot(shot2, ships2, hit2, miss2, done2)

    if missed2 == 1:
        tactics2 = calc_tactics(shot2, tactics2, guesses2, hit2)
    elif missed2 == 2:
        tactics2 = []
    elif len(tactics2) > 0:
        tactics2.pop(0)

    if check_if_empty_2(ships2):
        print("\nEnd of game - computer wins in", i)
        show_board(hit2, miss2, done2)
        break
