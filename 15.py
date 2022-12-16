import numpy as np

config = dict()


def check_row_stupid(y, remove=True, min_x=None, max_x=None):
    out2 = np.empty(shape=0)
    for beacon in config:
        for sensor in config[beacon]:
            d = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            if sensor[1] - d <= y <= sensor[1] + d:  # are we even at our line
                a = abs(sensor[1] - y)
                b = d - a
                start = sensor[0] - b if min_x is None else max(sensor[0] - b, min_x)
                stop = sensor[0] + b + 1 if max_x is None else min(sensor[0] + b + 1, max_x)
                tmp = np.arange(start=start, stop=stop)
                out2 = np.append(out2, tmp)

    if remove:
        for beacon in config:
            if beacon[1] == y:
                out2 = out2[out2 != beacon[0]]
            for sensor in config[beacon]:
                if sensor[1] == y:
                    out2 = out2[out2 != sensor[0]]
    return np.unique(out2)


def check_row_fast(y, min_x=None, max_x=None):
    intervals = []
    for beacon in config:
        for sensor in config[beacon]:
            d = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            if sensor[1] - d <= y <= sensor[1] + d:
                a = abs(sensor[1] - y)
                b = d - a
                start = sensor[0] - b if min_x is None else max(sensor[0] - b, min_x)
                stop = sensor[0] + b + 1 if max_x is None else min(sensor[0] + b + 1, max_x)
                intervals.append((start, stop))

    intervals.sort()
    min_x = intervals[0][0]
    max_x = intervals[0][1]

    for i in intervals[1:]:
        if min_x <= i[0] <= max_x:
            min_x = i[0]
            max_x = max(max_x, i[1])
        else:
            return False
    return True


if __name__ == "__main__":
    for row in open('inputs/input15', 'r').readlines():
        string = row.split(":")
        a = int(string[0].split("=")[1].split(",")[0])
        b = int(string[0].split("=")[2])

        c = int(string[1].split("=")[1].split(",")[0])
        d = int(string[1].split("=")[2])
        if (c, d) not in config:
            config[(c, d)] = []
        config[(c, d)].append((a, b))

    print("answer1", len(check_row_stupid(2000000)))

    m = 4000000
    for y in range(0, m + 1):
        if not check_row_fast(y, 0, m + 1):
            b = check_row_stupid(y, remove=False, min_x=0, max_x=m + 1)
            a = np.where(np.isin(np.array([x for x in range(0, m+1)]), b) == False)
            ans = a[0] * 4000000 + y
            print("answer2", ans[0])
            break
