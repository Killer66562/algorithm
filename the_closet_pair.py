from typing import Callable, Self
from math import pow, sqrt, inf
from random import random, randint
from statistics import median
from time import time


class Point(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, point: Self):
        return sqrt(pow((self.x - point.x), 2) + pow((self.y - point.y), 2))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
def the_closet_pair_slow(points: list[Point]) -> float:
    points_len = len(points)
    if points_len <= 1:
        return inf
    elif points_len == 2:
        return points[0].distance(points[1])
    else:
        d = inf
        for i in range(points_len - 1):
            for j in range(i + 1, points_len):
                d = min(d, points[i].distance(points[j]))
        return d
    
def create_points(n: int = 2000, x_range: int = 5000, y_range: int = 5000, force_int: bool = False) -> list[Point]:
    if force_int:
        zipped = zip((int(randint(-x_range, x_range) * random()) for _ in range(n)), (int(randint(-y_range, y_range) * random()) for _ in range(n)))
    else:
        zipped = zip((randint(-x_range, x_range) * random() for _ in range(n)), (randint(-y_range, y_range) * random() for _ in range(n)))
    return [Point(x, y) for x, y in zipped]

def the_closet_pair_recursive(points: list[Point]) -> float:
    points_len = len(points)
    if points_len == 1:
        return inf
    
    if points_len == 2:
        return points[0].distance(points[1])
    
    med = median([p.x for p in points])

    left = [p for p in points if p.x <= med]
    right = [p for p in points if p.x > med]

    if not left or not right:
        left = [p for p in points if p.x < med]
        right = [p for p in points if p.x >= med]

    if not left or not right:
        d = inf
        for i in range(points_len - 1):
            d = min(d, points[i].distance(points[i + 1]))

        return d
    
    print(left)
    print(right)
    
    dl = the_closet_pair_recursive(left)
    dr = the_closet_pair_recursive(right)

    d = min(dl, dr)
    ra = [p for p in left if p.x >= med - d]
    rb = [p for p in right if p.x <= med + d]

    for p1 in ra:
        filtered_rb = [p2 for p2 in rb if p2.y <= p1.y + d and p2.y >= p1.y + d]
        for p2 in filtered_rb:
            d = min(d, p1.distance(p2))

    return d


def the_closet_pair(points: list[Point]) -> float:
    points.sort(key=lambda p: (p.x, p.y))
    return the_closet_pair_recursive(points)

def timing(func: Callable, *args):
    start_time = time()
    func(*args)
    end_time = time()
    return end_time - start_time
    
def main():
    points = create_points(n=5000, x_range=10000, y_range=10000, force_int=True)
    print(timing(the_closet_pair_slow, points))

if __name__ == "__main__":
    main()