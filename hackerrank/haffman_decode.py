class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


def decode_haffman(root: Node, s: str):
    res = ''
    current = root
    for c in s:
        if c == '0':
            current = current.left
        else:
            current = current.right

        if current.data:
            res += current.data
            current = root
    print(res)


B = Node(1, 'B')
C = Node(1, "C")
BC = Node(2, "")
BC.left = B
BC.right = C
A = Node(3, 'A')
R = Node(5, "")
R.left = BC
R.right = A


def test_decode_haffman():
    decode_haffman(R, '1001011')

