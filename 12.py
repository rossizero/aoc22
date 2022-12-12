import numpy as np


def a_star(field, s, t):
    open_dict = dict()
    closed_dict = dict()
    parents = dict()

    open_dict[s] = 0

    found = False
    while len(open_dict) > 0 and not found:
        tmp = dict(sorted(open_dict.items(), key=lambda item: item[1]))
        q = next(iter(tmp))
        f = open_dict[q]
        open_dict.pop(q)
        neighbours = [(q[0] - 1, q[1]), (q[0] + 1, q[1]), (q[0], q[1] - 1), (q[0], q[1] + 1)]
        for n in neighbours:
            if 0 <= n[0] < field.shape[0] and 0 <= n[1] < field.shape[1]:
                diff = field[n] - field[q]
                if diff < 2:
                    # target found
                    if n == t:
                        found = True
                    nf = f + 1  # + math.sqrt((n[0] - t[0])**2 + (n[1] - t[1])**2) unsure why unnecessary

                    skip = False
                    if n in open_dict and open_dict[n] < nf:
                        skip = True

                    if n in closed_dict and closed_dict[n] < nf:
                        skip = True

                    if not skip:
                        parents[n] = q
                        open_dict[n] = nf
        closed_dict[q] = f

    curr = t
    count = 0
    while curr != s:
        curr = parents[curr]
        count += 1

    return count


if __name__ == "__main__":
    data = open('inputs/input12', 'r').readlines()
    field = np.array([[ord(a) - 97 for a in line.replace("\n", "")] for line in data])

    s = np.where(field == -14)
    s = list(zip(s[0], s[1]))[0]
    field[s] = 1

    t = np.where(field == -28)
    t = list(zip(t[0], t[1]))[0]
    field[t] = 25

    print("answer1:", a_star(field, s, t))

    arr = list(zip(np.where(field == 1)[0], np.where(field == 1)[1]))
    m = min([a_star(field, a, t) for a in arr]) + 1
    print("answer2:", m)
