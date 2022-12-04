if __name__ == "__main__":
    data = open('inputs/input1', 'r').readlines()

    s = 0
    arr = []
    for line in data:
        if line != "\n":
            s += int(line)
        else:
            arr.append(s)
            s = 0

    arr.sort(reverse=True)
    print("answer 1", arr[0])
    print("answer 2", (arr[0]+arr[1]+arr[2]))
