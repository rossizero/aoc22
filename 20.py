def f(arr, n):
    tmp = arr.copy()

    for _ in range(n):
        for i, a in arr:
            pos = tmp.index((i, a))
            tmp.remove((i, a))
            new_pos = (pos + a) % len(tmp)
            tmp.insert(new_pos, (i, a))

            if a == 0:
                null = (i, 0)

    vals = [tmp[(tmp.index(null) + n * 1000) % len(tmp)][1] for n in range(1, 4)]
    return sum(vals)


if __name__ == "__main__":
    nums = [(i, int(n)) for i, n in enumerate(open('inputs/input20', 'r').readlines())]
    nums2 = [(i, int(n) * 811589153) for i, n in enumerate(open('inputs/input20', 'r').readlines())]
    print("answer1", f(nums, 1))
    print("answer2", f(nums2, 10))
