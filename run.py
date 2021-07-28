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


hit = [1, 2]
miss = [4]
done = [3]
show_board(hit, miss, done)