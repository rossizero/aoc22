def convert(string):
    arr = []
    i = 1
    num = ""  # numbers > 9 exist in input... but not in example o.O
    while i < len(string):
        c = string[i]
        if c == "[":
            a, j = convert(string[i:])
            arr.append(a)
            i += j
        elif c == "]":
            if num != "":
                arr.append(int(num))
            return arr, i
        elif c != ",":
            num += c
        else:
            if num != "":
                arr.append(int(num))
                num = ""
        i += 1


def comp(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            return a - b  # comparing a < b is not enough because we need to continue if a == b -> 3 cases
        elif isinstance(b, list):
            return comp([a], b)
    elif isinstance(a, list):
        if isinstance(b, int):
            return comp(a, [b])
        elif isinstance(b, list):
            for i, item in enumerate(a):
                item2 = b[i] if i < len(b) else None
                if item2 is not None:
                    t = comp(item, item2)
                    if t < 0 or t > 0:  # if not the same, else continue
                        return t
                else:
                    return 1  # right side ran out of items
    return len(a) - len(b)  # comparing len(a) < len(b) is not enough... same argument


if __name__ == "__main__":
    data = [l.strip() for l in open('inputs/input13', 'r').readlines()]
    data.append("")

    a, b = None, None
    i = 1
    count = 0

    part2 = []
    for line in data:
        if line.strip() == "":
            tmp = comp(a, b)
            if tmp < 0:
                count += i
            a, b = None, None
            i += 1
        else:
            # prepare for default string sort
            part2.append(line.replace("[]", "0").replace("[", "").replace("]", "").replace("10", "a"))
            if a is None:
                a, _ = convert(line)
            else:
                b, _ = convert(line)

    print("answer1", count)

    part2.append("2")
    part2.append("6")
    part2.sort()
    print("answer2", (part2.index("2") + 1) * (part2.index("6") + 1))
