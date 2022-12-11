import numpy as np


if __name__ == "__main__":
    data = open('inputs/input10', 'r').readlines()

    x = 1
    cycle = 1
    signal = []
    image = np.zeros(shape=(6, 40), dtype=str)

    val = 0
    for i, line in enumerate(data):
        wait = 1

        if "addx" in line:
            cmd, val = line.split(" ")
            wait = 2

        for _ in range(wait):
            pixel = ((cycle-1) % 40, (cycle-1)//40)
            image[pixel[1], pixel[0]] = " "
            if pixel[0] in [x-2, x-1, x]:
                image[pixel[1], pixel[0]] = "#"

            cycle += 1
            if (cycle - 20) % 40 == 0 and cycle >= 20:
                signal.append(cycle * x)

            x += int(val)
            val = 0

    print("answer1:", sum(signal))
    print("answer2:")
    for line in image:
        var = ""
        for char in line:
            var += char
        print(var)
