"""
Implement a simple text editor. The editor initially contains an empty string, S.
Perform Q operations of the followIng 4 types:
1. append(W) - Append string W to the end of S.
2. delete(k) - Delete the last k characters of S.
3. print(k) - Print the eh character of S.
4. undo() - Undo the last (not previously undone) operation of type 1 or 2, reverting Soothe state it was in prior to that operation.

"""

class TextEditor:
    def __init__(self):
        self.text = ""
        self.operations = []

    def append(self, W):
        self.operations.append(self.text)
        self.text += W

    def delete(self, k):
        self.operations.append(self.text)
        self.text = self.text[:-k]

    def print_char(self, k):
        print(self.text[k - 1])

    def undo(self):
        if self.operations:
            self.text = self.operations.pop()

# Example usage
editor = TextEditor()

Q = int(input("Enter number of operations: "))
for _ in range(Q):
    operation = input().split()

    if operation[0] == "1":
        editor.append(operation[1])
    elif operation[0] == "2":
        editor.delete(int(operation[1]))
    elif operation[0] == "3":
        editor.print_char(int(operation[1]))
    elif operation[0] == "4":
        editor.undo()


text = ""
commands = []


def apply_command(command):
    global text, commands
    command, arg = int(command[0]), command[1]
    if command == 1:
        text += arg
        commands.append([command, len(arg)])
    elif command == 2:
        k = int(arg)
        commands.append([command, text[len(text)-k:]])
        text = text[:-k]
    elif command == 3:
        k = int(arg)
        print(text[k - 1])
    elif command == -1:
        k = arg
        text = text[:-k]
    elif command == -2:
        text += arg


# q = int(input("how many:"))
q = 7
# inputs = [
#     "1 fg", "3 6", "2 5", "4", "3 7", "4", "3 4"
# ]
inputs = [
    "1 abc",
    "3 3",
    "2 3",
    "1 xy",
    "3 2",
    "4",
    "4",
    "3 1"
]
for i in range(q):
    # command = input().split()
    command = inputs[i].split()
    if len(command) == 2:
        # commands.append(command)
        apply_command(command)
    else: # undo
        command = commands.pop()
        command[0] *= -1
        apply_command(command)
