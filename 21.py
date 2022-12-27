from copy import deepcopy

func = {"*": (lambda x, y: x * y),
        "/": (lambda x, y: x // y),
        "+": (lambda x, y: x + y),
        "-": (lambda x, y: x - y)}


def one(done: dict, link: dict, todo: dict):
    while "root" not in done.keys():
        # go over all monkeys in done, and look up their usages in todo via link
        # then calculate all todos with 2 numbers add to done and remove them from todo
        for a in list(done.keys()):
            if a in link.keys():
                for b in link[a]:
                    if todo[b][0] == a:
                        todo[b][0] = done[a]
                    elif todo[b][1] == a:
                        todo[b][1] = done[a]

                    if isinstance(todo[b][0], (float, int)) and isinstance(todo[b][1], (float, int)):
                        done[b] = func[todo[b][2]](todo[b][0], todo[b][1])
                        del todo[b]
                del link[a]
    return done["root"]


def two(done: dict, link: dict, todo: dict):
    del done["humn"]
    # same as part one, except we stop at first number of root
    # (given only one number depends on the value of humn)
    stop = False
    val = None
    while not stop:
        for a in list(done.keys()):
            if a in link.keys():
                for b in link[a]:
                    if todo[b][0] == a:
                        todo[b][0] = done[a]
                    elif todo[b][1] == a:
                        todo[b][1] = done[a]

                    if b == "root":
                        val = todo[b]
                        stop = True
                        break

                    if isinstance(todo[b][0], (float, int)) and isinstance(todo[b][1], (float, int)):
                        done[b] = func[todo[b][2]](todo[b][0], todo[b][1])
                        del todo[b]
                del link[a]

    # starting from root, going backwards
    right = 0 if isinstance(val[0], (float, int)) else 1  # check if value is at right or left position
    v = val[right]  # value at root
    next = val[1 - right]  # name of monkey (other position is the value we already know)

    while next != "humn":
        val = todo[next]
        right = 0 if isinstance(val[0], (float, int)) else 1
        num = val[right]
        operation = todo[next][2]

        # reverse operation
        if operation == "-":
            v = func["+"](v, num) if right else func["-"](num, v)
        elif operation == "/":
            # second case never happens with my input
            v = func["*"](v, num) if right else func["/"](num, v)
        elif operation == "+":
            v = func["-"](v, num)
        elif operation == "*":
            v = func["/"](v, num)
        next = val[1 - right]
    return v


def do():
    done = {}  # for monkeys shouting numbers
    todo = {}  # for monkeys shouting operations
    link = {}  # maps between a monkey and the monkeys that want to use its value at some point

    for monkey in open('inputs/input21', 'r').readlines():
        name, stuff = monkey.strip().split(":")
        if len(stuff.split(" ")) > 2:
            if "*" in stuff:
                m1, m2 = stuff.split("*")
                todo[name] = [m1.strip(), m2.strip(), "*"]
            elif "+" in stuff:
                m1, m2 = stuff.split("+")
                todo[name] = [m1.strip(), m2.strip(), "+"]
            elif "-" in stuff:
                m1, m2 = stuff.split("-")
                todo[name] = [m1.strip(), m2.strip(), "-"]
            elif "/" in stuff:
                m1, m2 = stuff.split("/")
                todo[name] = [m1.strip(), m2.strip(), "/"]

            if m1.strip() not in link:
                link[m1.strip()] = []
            if m2.strip() not in link:
                link[m2.strip()] = []
            link[m1.strip()].append(name)
            link[m2.strip()].append(name)
        else:
            done[name] = int(stuff)

    print("answer1", one(deepcopy(done), deepcopy(link), deepcopy(todo)))
    print("answer2", two(deepcopy(done), deepcopy(link), deepcopy(todo)))


if __name__ == "__main__":
    do()
