print("             Battleships        \n")
print("     0  1  2  3  4  5  6  7  8  9")

for x in range(10):
    row = ""
    for y in range(10):
        ch = " _ "
        row = row + ch
    print(x, " ", row)
