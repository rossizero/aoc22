from copy import deepcopy

if __name__ == "__main__":
    data = open('inputs/input5', 'r').readlines()

    operations = False
    stack_dict = {}
    stack_dict_part_a = {}
    stack_dict_part_b = {}

    for line in data:
        if line == "\n":
            operations = True
            stack_dict_part_a = deepcopy(stack_dict)
            stack_dict_part_b = deepcopy(stack_dict)
        # populate dict with crates
        if not operations:
            if "[" in line:
                for i in range(0, len(line), 4):
                    load = line[i + 1]
                    if (i / 4 + 1) not in stack_dict.keys():
                        stack_dict[i / 4 + 1] = []
                    if load != " ":
                        stack_dict[i / 4 + 1].append(load)
        # move crates around
        else:
            if "move" in line:
                small_line = line.replace("move ", "").replace("from ", "").replace("to ", "")
                a, b, c = small_line.split(" ")

                # CrateMover  9000
                for i in range(int(a)):
                    tmp = stack_dict_part_a[int(b)].pop(0)
                    stack_dict_part_a[int(c)].insert(0, tmp)

                # CrateMover  9001
                for i in range(int(a)):
                    tmp = stack_dict_part_b[int(b)].pop(int(a) - 1 - i)
                    stack_dict_part_b[int(c)].insert(0, tmp)

    # print solution
    s = ""
    s2 = ""
    for key in stack_dict.keys():
        s += stack_dict_part_a[key].pop(0)
        s2 += stack_dict_part_b[key].pop(0)

    print("answer 1:", s)
    print("answer 1:", s2)
