from statistics import median
from random import randint
from typing import Callable
from time import time


class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.rank = 0

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}) => rank: {self.rank}"

def mininum_2d_ranking_slow(arr: list[Point]):
    for p1 in arr:
        for p2 in arr:
            if p1.x > p2.x and p1.y > p2.y:
                p1.rank += 1

def mininum_2d_ranking_fast(arr: list[Point]) -> None:
    n = len(arr)
    if n <= 1:
        return
    
    med = median([p.x for p in arr])
    a = [p for p in arr if p.x <= med]
    b = [p for p in arr if p.x > med]

    if not a or not b:
        a = [p for p in arr if p.x < med]
        b = [p for p in arr if p.x >= med]

    if a and b:
        a_len = len(a)

        mininum_2d_ranking_fast(a)
        mininum_2d_ranking_fast(b)

        a.sort(key=lambda p: p.y)
        b.sort(key=lambda p: p.y)

        a_idx = 0
        for p in b:
            while a_idx < a_len and a[a_idx].y < p.y:
                a_idx += 1
            p.rank += a_idx

        arr = a + b

def timing(func: Callable, *args) -> float:
    start_time = time()
    func(*args)
    end_time = time()
    return end_time - start_time

def sort_and_compare_arr(arr1: list[Point], arr2: list[Point]) -> bool:
    arr1.sort(key=lambda p: (p.x, p.y), reverse=True)
    arr2.sort(key=lambda p: (p.x, p.y), reverse=True)

    arr1_len = len(arr1)
    arr2_len = len(arr2)

    if arr1_len != arr2_len:
        return False
    
    for i in range(arr1_len):
        p1 = arr1[i]
        p2 = arr2[i]
        if p1.x != p2.x or p1.y != p2.y or p1.rank != p2.rank:
            return False
    else:
        return True

def main():
    n = 20000
    min_val = -100000
    max_val = 100000
    arr1 = [Point(x, y) for x, y in zip((randint(min_val, max_val) for _ in range(n)), (randint(min_val, max_val) for _ in range(n)))]
    arr2 = [Point(p.x, p.y) for p in arr1]

    print(timing(mininum_2d_ranking_slow, arr1))
    print(timing(mininum_2d_ranking_fast, arr2))

    same = sort_and_compare_arr(arr1, arr2)

    '''
    for p in arr1:
        print(p)

    print()

    for p in arr2:
        print(p)

    print()
    '''

    print(same)

if __name__ == "__main__":
    main()