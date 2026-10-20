max_ln = []

while True:
    s = input()
    if s.lower() == "stop":
        break
    if not len(max_ln):
        max_ln.append(s)
        max_ln.append(len(set(s.lower())))
    else:
        if len(set(list(s.lower()))) > max_ln[-1]:
            max_ln[0] = s
            max_ln[1] = len(set(s.lower()))

print(max_ln[0], max_ln[1])
