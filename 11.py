import math

monkeys = []
prime_product = 1


class Monkey:
    def __init__(self):
        self.items = []
        self.operation = None
        self.test = None
        self.true = -1
        self.false = -1
        self.counter = 0

    def do(self):
        self.counter += len(self.items)
        for item in self.items:
            worry = self.operation(item)
            worry = math.floor(worry / 3.0)
            if self.test(worry):
                monkeys[self.true].items.append(worry)
            else:
                monkeys[self.false].items.append(worry)
        self.items.clear()  # no monkey throws to itself

    def do2(self):
        self.counter += len(self.items)
        for item in self.items:
            worry = self.operation(item)
            # if we reach the prime_product, we can just reset the worry counter.
            # monkey assignment "rate" stays the same and self.test of all monkeys would return true at this number
            worry = worry % prime_product
            if self.test(worry):
                monkeys[self.true].items.append(worry)
            else:
                monkeys[self.false].items.append(worry)
        self.items.clear()  # no monkey throws to itself


def init_monkeys():
    global prime_product
    global monkeys

    data = open('inputs/input11', 'r').readlines()

    monkeys.clear()
    prime_product = 1

    for i in range(0, len(data), 7):
        monkey = Monkey()
        items = data[i + 1].replace("Starting items: ", "").split(",")
        monkey.items = [int(item) for item in items]

        op, var2 = data[i + 2].replace("  Operation: new = old ", "").split(" ")
        if "*" in op:
            if "old" in var2:
                monkey.operation = lambda old: old * old
            else:
                monkey.operation = (lambda tmp: lambda old: old * tmp)(int(var2))  # again what learned...
        elif "+" in op:
            if "old" in var2:
                monkey.operation = lambda old: old + old
            else:
                monkey.operation = (lambda tmp: lambda old: old + tmp)(int(var2))  # again what learned...

        div = int(data[i + 3].replace("  Test: divisible by ", ""))
        prime_product *= div

        monkey.test = (lambda div: lambda worry: worry % div == 0)(div)

        monkey.true = int(data[i + 4].replace("    If true: throw to monkey ", ""))
        monkey.false = int(data[i + 5].replace("    If false: throw to monkey ", ""))
        monkeys.append(monkey)


if __name__ == "__main__":
    # part 1
    init_monkeys()
    for r in range(20):
        for monkey in monkeys:
            monkey.do()

    counters = [m.counter for m in monkeys]
    counters.sort()
    print("answer1", counters[-1] * counters[-2])

    # part 2
    init_monkeys()
    for r in range(1, 10001):
        for monkey in monkeys:
            monkey.do2()

    counters = [m.counter for m in monkeys]
    counters.sort()
    print("answer2", counters[-1] * counters[-2])
