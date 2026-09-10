with open("task7.txt") as f:
    for i in f:
        for symb in ".,!?:;":
            i.replace(symb, "")
        words = i.split()
        print(words)
