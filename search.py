from random import randint
from queue import Queue, PriorityQueue, LifoQueue
from typing import Self


class Tree(object):
    def __init__(self, value: int):
        self._value: int = value
        self._children: list[Self] = list()

    def __lt__(self, tree: Self):
        return self._value < tree._value
    
    def __gt__(self, tree: Self):
        return self._value > tree._value
    
    def __eq__(self, tree: Self):
        return self._value == tree._value

    @property
    def value(self) -> int:
        return self._value
    
    @property
    def is_leaf(self) -> bool:
        return not self._children

    def add_child(self, child: Self) -> None:
        self._children.append(child)

    def remove_child(self, child: Self) -> None:
        self._children.remove(child)

    def bfs(self) -> None:
        queue: Queue[Self] = Queue()
        queue.put(self)
        while not queue.empty():
            current = queue.get()
            print(current._value)
            for child in current._children:
                queue.put(child)

    def dfs(self) -> None:
        queue: LifoQueue[Self] = LifoQueue()
        queue.put(self)
        while not queue.empty():
            current = queue.get()
            print(current._value)
            for child in current._children:
                queue.put(child)
        
    def mc(self) -> None:
        queue: LifoQueue[Self] = LifoQueue()
        queue.put(self)
        while not queue.empty():
            current = queue.get()
            print(current._value)
            for child in sorted(current._children, key=lambda c: c.value):
                queue.put(child)

    def bestfs(self) -> None:
        queue: PriorityQueue[Self] = PriorityQueue()
        queue.put(self)
        while not queue.empty():
            current = queue.get()
            print(current._value)
            for child in current._children:
                queue.put(child)

def create_tree_rec(tree: Tree, current_depth: int, min_value: int, max_value: int, depth: int, max_childern: int) -> None:
    if current_depth >= depth:
        return None
    for _ in range(randint(1, max_childern)):
        child = Tree(randint(min_value, max_value))
        create_tree_rec(child, current_depth + 1, min_value, max_value, depth, max_childern)
        tree.add_child(child)

def create_tree(min_value: int = -1000, max_value: int = 1000, depth: int = 3, max_childern: int = 3) -> Tree:
    root = Tree(randint(min_value, max_value))
    create_tree_rec(root, 0, min_value, max_value, depth, max_childern)
    return root

def main():
    tree = create_tree()

    tree.bfs()
    print("========================")
    tree.dfs()
    print("========================")
    tree.mc()
    print("========================")
    tree.bestfs()

if __name__ == "__main__":
    main()

