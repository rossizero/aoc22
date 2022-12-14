import numpy as np


def line(x1, y1, x2, y2):
    for i in range(abs(x1 - x2) + 1):
        x = i + min(x1, x2)
        for j in range(abs(y1 - y2) + 1):
            y = j + min(y1, y2)
            if y not in input.keys():
                input[y] = set()
            input[y].add(x)


if __name__ == "__main__":
    input = dict()
    for row in open('inputs/input14', 'r').readlines():
        x1, y1, x2, y2 = -1, -1, -1, -1
        for num in row.strip().split(" -> "):
            x1, y1 = int(num.split(",")[0]), int(num.split(",")[1])
            if x2 != -1:
                line(x1, y1, x2, y2)
            x2, y2 = x1, y1

    cave = np.zeros(shape=(max(input.keys()) + 1, max([max(n[1]) for n in input.items()]) + 1))
    cave2 = np.zeros(shape=(max(input.keys()) + 2, max([max(n[1]) for n in input.items()]) * 2 + 1))
    cave2 = np.vstack([cave2, [1 for _ in range(max([max(n[1]) for n in input.items()]) * 2 + 1)]])

    for key in input:
        for x in input[key]:
            cave[key, x] = 1
            cave2[key, x] = 1

    done = False
    counter = 0
    while not done:
        counter += 1
        sand = (0, 500)
        step = True

        while step:
            neighbours = [(sand[0] + 1, sand[1]), (sand[0] + 1, sand[1] - 1), (sand[0] + 1, sand[1] + 1)]
            step = False
            for pos in neighbours:
                if 0 <= pos[0] < cave.shape[0] and 0 <= pos[1] < cave.shape[1]:
                    if cave[pos] == 0:
                        sand = pos
                        step = True
                        break
                else:
                    done = True
            if not step:
                cave[sand] = 2

    print("answer1:", counter - 1)

    counter = 0
    while not cave2[(0, 500)] == 2:
        counter += 1
        sand = (0, 500)
        step = True

        while step:
            neighbours = [(sand[0] + 1, sand[1]), (sand[0] + 1, sand[1] - 1), (sand[0] + 1, sand[1] + 1)]
            step = False
            for pos in neighbours:
                if 0 <= pos[0] < cave2.shape[0] and 0 <= pos[1] < cave2.shape[1]:
                    if cave2[pos] == 0:
                        sand = pos
                        step = True
                        break
            if not step:
                cave2[sand] = 2

    print("answer2:", counter)
