import random

def main(size):
    maze = [
        [(x in (0, size-1) or y in (0, size-1)) for x in range(size)]
        for y in range(size)
    ]

    
    # ----- only dots -----
    # for y in range(2, size-2, 2):
    #     for x in range(2, size-2, 2):
    #         maze[y][x] = 1


    # for y in range(2, size-2, 2):
    #     for x in range(2, size-2, 2):
    #         d = [0, 0]
    #         d[random.randint(0, 1)] = random.choice((-1, 1))
            
    #         maze[y][x] = 1
    #         maze[y + d[1]][x + d[0]] = 1

    pivots = [(x, y) for x in range(2, size-2, 2) for y in range(2, size-2, 2)]
    random.shuffle(pivots)
    available_pivots = set(pivots)

    going = False
    while len(available_pivots)>0:
        if going:
            d = rand_turn(d)
            available_pivots.remove(pivot)
        else:
            d = rand_dir()
            pivot = available_pivots.pop()

        maze[pivot[1]][pivot[0]] = 1
        
        half_p = (pivot[0]+d[0], pivot[1]+d[1])
        pivot  = (half_p[0]+d[0], half_p[1]+d[1])

        maze[half_p[1]][half_p[0]] = 1

        going = pivot in available_pivots and is_in(pivot, size)

    return maze

def is_in(p, size):
    return (p[0] > 0 and p[0] < size-1) and (p[1] > 0 and p[1] < size-1)

def rand_dir():
    d = [0, 0]
    d[random.randint(0, 1)] = random.choice((-1, 1))
    return d

def rand_turn(d):
    r = random.choice([-1, 1])
    if random.randint(0, 1):
        return (r*(d[0]==0), r*(d[1]==0))
    else:
        return d


def display2d(m):
    for row in m:
        for x in row:
            print(1 if x else 0, end=" ")
        print()

if __name__ == "__main__":
    display2d(main(11))