from functools import cache, lru_cache


def insertion_sort(arr: list[float], n: int = -1):
    if n < 0:
        n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

def quick_sort(arr: list[float], start: int, stop: int):
    if stop - start <= 1:
        return

    s_idx = start
    p_idx = start

    for i in range(start + 1, stop):
        if arr[i] < arr[p_idx]:
            if p_idx == s_idx:
                p_idx = i
            arr[i], arr[s_idx] = arr[s_idx], arr[i]
            s_idx += 1
        
    arr[s_idx], arr[p_idx] = arr[p_idx], arr[s_idx]

    quick_sort(arr, 0, s_idx)
    quick_sort(arr, s_idx + 1, stop)

with open("test2.txt", mode="r", encoding="utf-8") as file:
    file_in = file.read()

arr = list(map(float, file_in.split(" ")))

quick_sort(arr, 0, 30)

print(arr[:30])