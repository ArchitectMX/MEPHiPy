class CommandProcessor:
    def __init__(self):
        self.numb = 0


class Add:
    def exec(self):
        pass


class Multiply:
    def exec(self):
        pass    


class Subtract:
    def exec(self):
        pass


class Divide:
    def exec(self):
        pass


commands = {
    "add": Add,
    "subtract": Subtract,
    "multiply": Multiply,
    "divide": Divide,
    "exit": None,
    "histoty": None,
}


while True:
    command = input().split()
    if command[0] not in commands.keys():
        print(f"invalid command: {command[0]}")
        continue
    if command[0] == "exit":
        break


