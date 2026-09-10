import random


numb = 0


mean = 0
students = 0
maxScore = -float("inf")
minScroe = float("inf")
name = ""
countOfLochs = 0
with open("task6.csv") as f:
    for i in f:
        students += 1
        line = i.strip().split(";")
        try:
            score = int(line[-1])
            mean += score
            minScroe = min(minScroe, score)
            maxScore = max(maxScore, score)
            if score == maxScore:
                name = line[0]
            if score < 60:
                countOfLochs += 1
        except:
            print(f"in string {students} not a number")


mean = mean / students

print(mean)
print(maxScore)
print(minScroe)
print(name)
print(countOfLochs)


def addStudent(line):
    with open("task6.csv") as f:
        f.write(f"{line}\n")


# использована заглушка функции т.к не подключал библиотеку
def Faker():
    numb += 1
    return f"name{numb} surname{numb}"


def createStudent():
    name = Faker()
    mark = str(random.randint(1, 100))
    return name + mark






