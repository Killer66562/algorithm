from random import randint


class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


def convex_hull(points: list[Point]) -> list[Point]:
    sorted_points = sorted(points, key=lambda point: (point.x, point.y))
    
    wall_points = []
    idx = 0
    current_point = None

    


def counting_sort(arr: list[int]):
    arr_min = min(arr)
    arr_max = max(arr)

    mapping = [0 for _ in range(arr_min, arr_max + 1)]
    for num in arr:
        mapping[num - arr_min] += 1

    idx = 0
    for i in range(arr_min, arr_max + 1):
        if mapping[i - arr_min] <= 0:
            continue
        for _ in range(mapping[i - arr_min]):
            arr[idx] = i
            idx += 1

def main():
    points = [Point(x=randint(0, 9), y=randint(0, 9)) for _ in range(20)]
    convex_hull(points=points)

if __name__ == '__main__':
    main()