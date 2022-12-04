if __name__ == "__main__":
    data = open('inputs/input2', 'r').readlines()
    # points
    # 1 rock A X
    # 2 paper B Y
    # 3 scissors C Z
    # 0 loose
    # 3 draw
    # 6 win

    score = 0

    for line in data:
        opponent, me = line.split(" ")
        me = me[0]
        round_score = 0
        if opponent == 'A':
            if me == 'X':
                round_score = 1 + 3
            elif me == 'Y':
                round_score = 2 + 6
            elif me == 'Z':
                round_score = 3 + 0
        elif opponent == 'B':
            if me == 'X':
                round_score = 1 + 0
            elif me == 'Y':
                round_score = 2 + 3
            elif me == 'Z':
                round_score = 3 + 6
        elif opponent == 'C':
            if me == 'X':
                round_score = 1 + 6
            elif me == 'Y':
                round_score = 2 + 0
            elif me == 'Z':
                round_score = 3 + 3

        score += round_score

    print(score)

    score = 0
    # x loose
    # y draw
    # z win

    for line in data:
        opponent, me = line.split(" ")
        me = me[0]
        round_score = 0
        if opponent == 'A':
            if me == 'X':
                round_score = 3 + 0
            elif me == 'Y':
                round_score = 1 + 3
            elif me == 'Z':
                round_score = 2 + 6
        elif opponent == 'B':
            if me == 'X':
                round_score = 1 + 0
            elif me == 'Y':
                round_score = 2 + 3
            elif me == 'Z':
                round_score = 3 + 6
        elif opponent == 'C':
            if me == 'X':
                round_score = 2 + 0
            elif me == 'Y':
                round_score = 3 + 3
            elif me == 'Z':
                round_score = 1 + 6

        score += round_score

    print(score)
