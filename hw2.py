from typing import Self, Callable
from time import time
from random import randint


class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.rank = 0

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}) => Rank: {self.rank}"
    
    def __gt__(self, point: Self) -> bool:
        return self.x > point.x and self.y > point.y
    
    def __eq__(self, point: Self) -> bool:
        return self.x == point.x and self.y == point.y
    
    def __lt__(self, point: Self) -> bool:
        return self.x < point.x and self.y < point.y


def rank_slow(arr: list[Point]):
    for p1 in arr:
        for p2 in arr:
            if p1 > p2:
                p1.rank += 1

def rank_medium(arr: list[Point]):
    arr.sort(key=lambda p: (p.x, p.y), reverse=True)
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i].rank += 1

def rank_fast(arr: list[Point]):
    n = len(arr)
    if n <= 1:
        return
    else:
        arr.sort(key=lambda p: (p.x, p.y)) #O(nlog(n))
        med = n // 2

        rank_fast(arr[0:med])
        rank_fast(arr[med:n])

        count = 0

        for p1 in arr[med:n]:
            for p2 in arr[count:med]:
                if p1 > p2:
                    count += 1
                else: #提早退出
                    p1.rank += count
                    break
            else: #比後面的都來得大所以要加上count
                p1.rank += count

def timing(func: Callable, *args) -> float:
    start_time = time()
    func(*args)
    end_time = time()
    return end_time - start_time

def test(test_times: int = 5, n = 1000, min_val = -5000, max_val = 5000) -> None:
    for i in range(1, test_times + 1):
        arr1 = [Point(x, y) for x, y in zip((randint(min_val, max_val) for _ in range(n)), (randint(min_val, max_val) for _ in range(n)))]
        arr2 = [Point(p.x, p.y) for p in arr1]

        time_fast = timing(rank_fast, arr1)
        time_slow = timing(rank_slow, arr2)

        print(f"Test #{i} (fast): {time_fast} secs")
        print(f"Test #{i} (slow): {time_slow} secs")

        arr1.sort(key=lambda p: (p.x, p.y), reverse=True)
        arr2.sort(key=lambda p: (p.x, p.y), reverse=True)

        if arr1 != arr2:
            print("Test failed!")
            break
    else:
        print("Test passed")

def main():
    test(n=5000, min_val=-10, max_val=10)

if __name__ == "__main__":
    main()