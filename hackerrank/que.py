# q = int(input("1: "))
# print(q)
q = 10


def funcs(inp):
    q = int(input())
    que = []

    for i in range(q):
        inp = input()
        data = inp.split()
        if data[0] == '1':
            que.append(data[1])
        elif data[0] == '2':
            que.pop(0)
        else:
            print(que[0])


def test_func():
    funcs("1 42")
    funcs("2")
    funcs("1 14")
    funcs("3")
    funcs("1 28")
    funcs("3")
    funcs("1 60")
    funcs("1 78")
    funcs("2")
    funcs("2")
