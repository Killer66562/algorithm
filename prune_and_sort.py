from random import randint
from math import inf
from time import time
from typing import Any, Callable, T


def find_k_smallest(arr: list[float], k: int):
    arr_len = len(arr)
    if k >= arr_len:
        raise ValueError(f"There are only {arr_len} elements in array!")

    if arr_len <= 10:
        new_arr = sorted(arr, key=lambda x: x)
        return new_arr[k]

    subsets_count = len(arr) // 5 + (0 if arr_len % 5 == 0 else 1)
    subsets = [arr[5*i:5*(i+1)] for i in range(subsets_count)]
    last_subset_len = len(subsets[-1])

    while last_subset_len < 5:
        subsets[-1].append(inf)
        last_subset_len = last_subset_len + 1

    for s in subsets:
        s.sort(key=lambda x: x)
    med_subset = subsets[subsets_count // 2]
    med = med_subset[2]

    s1 = [x for x in arr if x < med]
    s2 = [x for x in arr if x == med]
    s3 = [x for x in arr if x > med]

    s1_len = len(s1)
    s2_len = len(s2)

    if k < s1_len:
        return find_k_smallest(s1, k)
    elif k < s1_len + s2_len:
        return find_k_smallest(s2, k - s1_len)
    else:
        return find_k_smallest(s3, k - s1_len - s2_len)
    
def find_k_smallest_sorted(arr: list[float], k: int):
    arr_len = len(arr)
    if k >= arr_len:
        raise ValueError(f"There are only {arr_len} elements in array!")
    
    new_arr = sorted(arr, key=lambda x: x)
    return new_arr[k]


def timing(func: Callable[...], *args) -> tuple[float, Any]:
    start_time = time()
    result = func(*args)
    end_time = time()
    return end_time - start_time, result

def main():
    arr = [randint(-10000000, 10000000) for _ in range(1000000)]

    k = 66

    not_sort_time, result1 = timing(find_k_smallest, arr, k)
    sort_time, result2 = timing(find_k_smallest_sorted, arr, k)

    print(not_sort_time)
    print(sort_time)

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()