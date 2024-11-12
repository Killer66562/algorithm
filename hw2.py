from statistics import median
from random import randint, random
from typing import Callable
from time import time


class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.rank = 0

    def __repr__(self) -> str:
        return "(%.2f %.2f) => rank: %d" % (self.x, self.y, self.rank)

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
    
def print_ranking_result(arr: list[Point]):
    for p in arr:
        print(p)

    print()
    arr.sort(key=lambda p: p.rank)

    arr_len = len(arr)
    print(f"Number of points: {arr_len}")

    min_rank_p = arr[0]
    max_rank_p = arr[-1]
    print(f"Max rank: {max_rank_p.rank}")
    print(f"Min rank: {min_rank_p.rank}")

    avr = sum([p.rank for p in arr]) / arr_len
    print("Average rank: %.2f" % (avr, ))
    
def create_test_data(n: int = 2000, min_val: int = -5000, max_val: int = 5000, filename: str = "test2.txt"):
    if n < 1:
        print("n >= 1 required")
        return

    arr = [Point(x, y) for x, y in zip((randint(min_val, max_val) * random() for _ in range(n)), (randint(min_val, max_val) * random() for _ in range(n)))]

    with open(file=filename, mode='w', encoding="utf8") as file:
        for p in arr:
            text = "%.2f %.2f\r\n" % (p.x, p.y)
            file.write(text)

    mininum_2d_ranking_slow(arr)
    print_ranking_result(arr)

def load_test_data_and_solve(filename: str = "test2.txt"):
    arr = []

    with open(file=filename, mode='r', encoding="utf8") as file:
        while True:
            try:
                x_y_str = file.readline()
                #Check EOF while using readline
                if not x_y_str:
                    break
                x_y_str = x_y_str.strip()
                #After strip, an empty string may appear
                if not x_y_str:
                    continue
                x_y_list = list(map(float, x_y_str.split()))
                x = x_y_list[0]
                y = x_y_list[1]
                arr.append(Point(x, y))
            except EOFError:
                break

    mininum_2d_ranking_fast(arr)
    print_ranking_result(arr)

def main():
    #create_test_data()
    load_test_data_and_solve()

if __name__ == "__main__":
    main()