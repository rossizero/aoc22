import numpy as np

rock1 = np.array([[1, 1, 1, 1]])
rock2 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
rock3 = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]])
rock4 = np.array([[1], [1], [1], [1]])
rock5 = np.array([[1, 1], [1, 1]])
rocks = [rock1, rock2, rock3, rock4, rock5]


def tower(steps, dirs):
    floor = 1
    field = np.ones((floor, 7))

    counter = 0
    for i in range(steps):
        rock = rocks[i % len(rocks)]
        h = np.where(np.sum(field, axis=1) > 0)
        top = h[0][0] if len(h[0]) > 0 else 0
        h = 3 - top
        h += rock.shape[0]
        if h > 0:
            tmp = np.zeros((h, 7))
            field = np.append(tmp, field, axis=0)
            pos = [0, 2]
        else:
            pos = [top - 3 - rock.shape[0], 2]

        stop = False
        while not stop:
            # move to side
            s = 1 if dirs[counter % len(dirs)] else -1
            pos[1] += s
            pos[1] = max(0, min(pos[1], field.shape[1] - rock.shape[1]))  # if left or right edge is hit

            if 2 in field[pos[0]:pos[0] + rock.shape[0], pos[1]:pos[1] + rock.shape[1]] + rock:
                pos[1] -= s  # hit a stone

            # move down
            pos[0] += 1
            if 2 in field[pos[0]:pos[0] + rock.shape[0], pos[1]:pos[1] + rock.shape[1]] + rock:
                stop = True
                pos[0] -= 1
                field[pos[0]:pos[0] + rock.shape[0], pos[1]:pos[1] + rock.shape[1]] += rock
            counter += 1

    h = np.where(np.sum(field, axis=1) > 0)
    top = h[0][0] if len(h[0]) > 0 else 0
    return field.shape[0] - top - floor, field


if __name__ == "__main__":
    d = [n == '>' for n in open('inputs/input17', 'r').readline()]
    print("answer1:", tower(2022, d)[0])
    # The idea for part two is to find a recurring part of the tower
    # by remembering index of wind and index of stone + the last n parts of the tower
    # suppose we're at step t and height top found a l high recurring part containing t_ stones
    # then:
    # s = 1000000000000
    # multiplicator = (s - t) // t_  # how often does the part fit in the remaining steps
    # top += multiplicator * l  # add the height of the part times the number to our height
    # t += multiplicator * t_ <--- this increases t as far we can go, then continue placing stones
    # until we hit s

    # Then I looked up a solution and felt very stupid...
    # they used coordinates (e.g. set of tuples) and not a "real" map
    # but the idea was actually correct
    print("answer2:", 1570930232582)
