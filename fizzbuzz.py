line = str("2 7 15")
print(line)
a, b, n = line.split(" ")
a = int(a)
b = int(b)
for i in range(1, int(n) + 1):
    if i % (a * b) == 0:
        print("FB ", end="")
    elif i % (a) == 0:
        print("A ", end="")
    elif i % (b) == 0:
        print("B ", end="")
    else:
        print(i, end=" ")

res = [
    "FB "
    if num % (a * b) == 0
    else "F "
    if num % (a) == 0
    else "B "
    if num % (b) == 0
    else num
    for num in range(1, int(n) + 1)
]
print(res)
