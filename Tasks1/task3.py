# n = list(map(int, input().split()))
n = [1, 1, 1, 2, 2, 5, 5, 5, 5, 3]
# n = [1]
# n = []


def group_lst(n):
    if not len(n):
        return 0
    count = 1
    res = []
    for i in range(len(n) - 1):
        if n[i] != n[i + 1]:
            res.append((n[i], count))
            count = 1
        else:
            count += 1
    res.append((n[-1], count))

    return res


def regroup_lst(n):
    if not len(n):
        return 0
    res = []
    for i in n:
        res.extend([i[0]] * i[1])
    return res


res = group_lst(n)
print(res)
print(regroup_lst(res))
