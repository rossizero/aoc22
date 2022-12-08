import numpy as np


def count(line):
    ret = np.zeros(line.shape)
    m = -1
    for i, val in enumerate(line):
        if val > m:
            m = val
            ret[i] = 1
    return ret


def scenic(x, y, forest):
    a = 0
    b = forest.shape[0] - 1
    c = 0
    d = forest.shape[1] - 1

    tmp = forest[y, x]
    # row
    for i, val in enumerate(forest[y]):
        if val >= tmp and i < x:
            a = i
        if val >= tmp and i > x:
            b = min(b, i)
    # column
    for i, val in enumerate(forest[:, x]):
        if val >= tmp and i < y:
            c = i
        if val >= tmp and i > y:
            d = min(d, i)
    return (x - a) * (b - x) * (y - c) * (d - y)


if __name__ == "__main__":
    data = open('inputs/input8', 'r').readlines()
    forest = np.array([np.array([int(i) for i in data[j].replace("\n", "")]) for j in range(len(data))])
    result = np.zeros(forest.shape)

    # forest is quadratic (99x99), otherwise rows and columns would have to be counted separately
    for j in range(len(forest)):
        row = forest[j]
        row2 = forest[j][::-1]
        column = forest[:, j]
        column2 = forest[:, j][::-1]

        result[j] += count(row)
        result[j] += count(row2)[::-1]
        result[:, j] += count(column)
        result[:, j] += count(column2)[::-1]

    print("answer1:", np.sum(result >= 1))

    for x in range(len(forest)):
        for y in range(len(forest)):
            result[y, x] = scenic(x, y, forest)

    print("answer2:", int(np.max(result)))




