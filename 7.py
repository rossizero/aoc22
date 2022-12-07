class Tree:
    def __init__(self, parent: 'Tree', name: str, size=0):
        self.children = {}
        self.parent = parent
        self.name = name
        self.size = size

    def total_size(self):
        if len(self.children) > 0:
            s = [self.children[key].total_size() for key in self.children]
            return sum(s)
        else:
            return self.size

    def answer1(self, arr):
        if len(self.children) > 0:
            s = [self.children[key].answer1(arr) for key in self.children]
            if sum(s) < 100000:
                arr.append(sum(s))
            return sum(s)
        else:
            return self.size

    def answer2(self, arr, val):
        if len(self.children) > 0:
            s = [self.children[key].answer2(arr, val) for key in self.children]
            if sum(s) > val:
                arr.append(sum(s))
            return sum(s)
        else:
            return self.size


if __name__ == "__main__":
    data = open('inputs/input7', 'r').readlines()
    folder = Tree(None, "/")
    current = folder

    for line in data[1:]:
        if "$" in line:
            cmd = line.replace("$ ", "").replace("cd ", "")
            if "ls" not in line:
                current = current.parent if ".." in cmd else current.children[cmd]
        else:
            t, name = line.split(" ")
            current.children[name] = Tree(current, name) if t == "dir" else Tree(current, name, int(t))

    arr = []
    folder.answer1(arr)
    print("answer1: ", sum(arr))

    needed_dir_size = 30000000 - (70000000 - folder.total_size())
    arr = []
    folder.answer2(arr, needed_dir_size)
    arr.sort()
    print("answer2: ", arr[0])
