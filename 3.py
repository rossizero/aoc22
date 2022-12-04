def val(char):
    char = ord(char)
    # a: 97 - z: 122
    # A: 65 - Z: 90

    if 65 <= char <= 90:
        return char - ord("A") + 27
    elif 97 <= char <= 122:
        return char - ord("a") + 1
    return 0


if __name__ == "__main__":
    data = open('inputs/input3', 'r').readlines()
    sum_single = 0
    for line in data:
        # shared stuff in single backpack
        one = line[:int(len(line)/2)]
        two = line[int(len(line)/2):]

        for char in one:
            if char in two:
                sum_single += val(char)
                two = two.replace(char, "")

    print(sum_single)

    group = []
    sum_group = 0
    for line in data:
        group.append(line)
        if len(group) == 3:
            for char in group[0]:
                if char in group[1] and char in group[2]:
                    sum_group += val(char)
                    group[1] = group[1].replace(char, "")
                    group[2] = group[2].replace(char, "")
            group = []
    print(sum_group)
