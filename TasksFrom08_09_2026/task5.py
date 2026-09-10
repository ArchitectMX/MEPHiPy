# lst = list(map(int, input().split()))
# k = int(input())

lst = [2, 4, 6, 8, 10]
k = 3

def meanK(lst, k):
    if k <= 0 or k > len(lst):
        return 0
    sumK = sum(lst[0:k])
    res = [sumK / k]
    for i in range(len(lst) - k):
        sumK = sumK - lst[i] + lst[i + k]
        res.append(sumK / k)
    return res


print(meanK(lst, k))


