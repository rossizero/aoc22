if __name__ == "__main__":
    data = open('inputs/input4', 'r').readlines()

    counter = 0
    for line in data:
        a, bc, d = line.split("-")
        b, c = bc.split(",")
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if a <= c and b >= d:
            counter += 1
        elif c <= a and d >= b:
            counter += 1

    print("answer 1: ", counter)

    counter = 0
    for line in data:
        a, bc, d = line.split("-")
        b, c = bc.split(",")
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if b >= c and d >= a:
            counter += 1

    print("answer 2: ", counter)
