if __name__ == "__main__":
    data = open('inputs/input6', 'r').readlines()[0]
    answer1 = False
    answer2 = False
    arr = []

    for i, char in enumerate(data):
        arr.append(char)
        arr = arr[-14:]

        if len(arr) >= 4 and not answer1:
            tmp = arr[-4:]
            s = [tmp.count(tmp[j]) for j in range(3)]
            if sum(s) == 3:
                print("answer 1", tmp, i + 1)
                answer1 = True

        if len(arr) == 14 and not answer2:
            s = [arr.count(arr[j]) for j in range(14)]
            if sum(s) == 14:
                print("answer 2", arr, i + 1)
                answer2 = True

        if answer1 and answer2:
            break
