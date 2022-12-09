def correct(head, tail):
    if head - tail > 0:
        return 1
    elif head - tail < 0:
        return -1
    else:
        return 0


def part1():
    data = open('inputs/input9', 'r').readlines()
    hx, hy = 0, 0
    tx, ty = 0, 0

    coords = set()
    coords.add((0, 0))

    for line in data:
        direction, steps = line.split(" ")
        steps = int(steps)
        for i in range(0, steps):
            if direction == "R":
                hx += 1
                if abs(hx - tx) > 1:
                    ty += correct(hy, ty)
                    tx += 1
            elif direction == "L":
                hx -= 1
                if abs(hx - tx) > 1:
                    ty += correct(hy, ty)
                    tx -= 1
            elif direction == "U":
                hy += 1
                if abs(hy - ty) > 1:
                    tx += correct(hx, tx)
                    ty += 1
            elif direction == "D":
                hy -= 1
                if abs(hy - ty) > 1:
                    tx += correct(hx, tx)
                    ty -= 1
            coords.add((tx, ty))
    print("answer1", len(coords))


def part2():
    data = open('inputs/input9', 'r').readlines()
    rope = [[0, 0] for _ in range(10)]
    coords = set()
    coords.add((0, 0))

    for line in data:
        direction, steps = line.split(" ")
        steps = int(steps)

        for i in range(0, steps):
            if direction == "R":
                rope[0][0] += 1
            elif direction == "L":
                rope[0][0] -= 1
            elif direction == "U":
                rope[0][1] += 1
            elif direction == "D":
                rope[0][1] -= 1

            last = rope[0]
            for knot in rope[1:]:
                if last[0] - knot[0] > 1:
                    knot[0] += 1
                    knot[1] += correct(last[1], knot[1])
                elif last[0] - knot[0] < -1:
                    knot[0] -= 1
                    knot[1] += correct(last[1], knot[1])

                if last[1] - knot[1] > 1:
                    knot[1] += 1
                    knot[0] += correct(last[0], knot[0])
                elif last[1] - knot[1] < -1:
                    knot[1] -= 1
                    knot[0] += correct(last[0], knot[0])
                last = knot
            coords.add((rope[len(rope) - 1][0], rope[len(rope) - 1][1]))
    print("answer2", len(coords))


if __name__ == "__main__":
    part1()
    part2()
