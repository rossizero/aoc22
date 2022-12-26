if __name__ == "__main__":
    edges = set()
    stones = set()

    for line in open('inputs/input18', 'r').readlines():
        a, b, c = line.strip().split(",")
        x = int(a)
        y = int(b)
        z = int(c)
        stones.add((x, y, z))
        edges_ = [(x+0.5, y, z), (x-0.5, y, z), (x, y+0.5, z), (x, y-0.5, z), (x, y, z+0.5), (x, y, z-0.5)]
        for edge in edges_:
            if edge in edges:
                edges.remove(edge)
            else:
                edges.add(edge)
    print("answer1", len(edges))

    min_ = (min(stones)[0]-1, min(stones, key=lambda t: t[1])[1]-1, min(stones, key=lambda t: t[2])[2]-1)
    max_ = (max(stones)[0]+1, max(stones, key=lambda t: t[1])[1]+1, max(stones, key=lambda t: t[2])[2]+1)

    water = set()
    visited = set()
    touched = set()
    water.add(min_)

    while len(water) > 0:
        x, y, z = water.pop()
        visited.add((x, y, z))
        neighbours = [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]
        for n in neighbours:
            if n in stones:
                edge = ((x+n[0])*0.5, (y+n[1])*0.5, (z+n[2])*0.5)
                touched.add(edge)
            elif n not in visited \
                    and min_[0] <= n[0] <= max_[0] \
                    and min_[1] <= n[1] <= max_[1] \
                    and min_[2] <= n[2] <= max_[2]:
                water.add(n)

    print("answer2", len(touched))
