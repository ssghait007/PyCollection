
moves = 0


def move(f, t):
    print("move disc from {} to {}".format(f, t))


def moveVia(f, v, t):
    move(f, v)
    move(v, t)


def hanoi(n, f, h, t):
    global moves
    if(n == 0):
        pass
    else:
        moves += 1
        hanoi(n-1, f, t, h)
        move(f, t)
        hanoi(n-1, h, f, t)


def print_moves():
    global moves
    print('moves required are {}'.format(moves))
