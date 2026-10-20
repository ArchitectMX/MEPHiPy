dots = [tuple(map(float, (i.split(", ")))) for i in input()[1:-1].split(") (")]
controlDot = list(map(float, input()[1:-1].split(", ")))

def nearestPoint(dots, controlDot):
    minDist = float("inf")
    minDot = None

    for x in dots:
        dst = (controlDot[0] - x[0]) ** 2 + (controlDot[1] - x[1]) ** 2

        if dst < minDist:
            minDot = x
            minDist = dst

    return minDot, minDist ** 0.5

# (1, 2) (3, 4) (5.5, 6.7)
# dots.sort(key=lambda x: (controlDot[0] - x[0]) ** 2 + (controlDot[1] - x[1]) ** 2)
# print(dots[0])

res = nearestPoint(dots, controlDot)

print(res)
