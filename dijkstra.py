from typing import Self
from math import sqrt, pow, inf
from random import sample


class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


    def distance(self, point: Self) -> float:
        return sqrt(pow(self.x - point.x, 2) + pow(self.y - point.y, 2))
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    

def main():
    k = 4
    n = 10

    x_pool = list(range(n))
    y_pool = list(range(n))

    points = [Point(x, y) for x, y in zip(sample(x_pool, k=k), sample(y_pool, k=k))]

    print(points)

    visited = [False for _ in points]
    distances = [inf for _ in points]
    board = [[p2.distance(p1) for p2 in points] for p1 in points]

    for i in range(k):
        visited[i] = True
        for j in range(k):
            if j <= i:
                continue
            old_dis = 0 if i == 0 else inf
            distances[j] = min(distances[j], old_dis + board[i][j])

    for l in board:
        print(l)

    print(distances)

if __name__ == "__main__":
    main()