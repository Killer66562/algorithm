from typing import Self


class Node(object):
    def __init__(self, left: Self | None = None, right: Self | None = None, freq: int = 0) -> None:
        self.left = left
        self.right = right
        self.freq = freq
        self.code = ""

def build_tree(text: str) -> Node:
    char_list = list(text)
    table = {}
    for char in char_list:
        if not table.get(char):
            table[char] = 0
        table[char] += 1
    nodes = [Node(freq=table[key]) for key in table]
    while len(nodes) > 1:
        left = min(nodes, key=lambda n: n.freq)
        nodes.remove(left)
        right = min(nodes, key=lambda n: n.freq)
        nodes.remove(right)
        node = Node(left=left, right=right, freq=left.freq+right.freq)
        nodes.append(node)
    root = nodes[0]

    

def encode(text: str) -> None: ...