n, m = list(map(int, input().split()))


def spiral(n, m):
    matrix = [[0] * n for _ in range(m)]

    top, left, right, bottom = 0, 0, n - 1, m - 1

    step, numb = 1, 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = numb
            numb += 1

        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = numb
            numb += 1

        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = numb
                numb += 1

            bottom -=1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = numb
                numb += 1

            left += 1

    return matrix


mtr = spiral(n, m)
for i in (mtr):
    for k in (i):
        print(f'{k:3}', end=' ')
    print()


