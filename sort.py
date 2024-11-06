import random


def insertion_sort(arr: list[float]) -> None:
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

def selection_sort(arr: list[float]) -> None:
    n = len(arr)
    for i in range(n - 1):
        flag = i
        for j in range(i + 1, n):
            if arr[j] < arr[flag]:
                flag = j
        arr[i], arr[flag] = arr[flag], arr[i]

def quick_sort(arr: list[float], start: int, end: int) -> None:
    if start >= end:
        return

    end_ori = end
    pivot = arr[0]
    start_turn = True
    switched = False
    while start < end:
        if start_turn:
            if arr[start] >= pivot:
                if switched:
                    start_turn = False
                    switched = False
                else:
                    arr[start], arr[end] = arr[end], arr[start]
                    switched = True
                    start += 1
                    end -= 1
            else:
                start += 1
        else:
            if arr[end] <= pivot:
                if switched:
                    start_turn = True
                    switched = False
                else:
                    arr[start], arr[end] = arr[end], arr[start]
                    switched = True
                    start += 1
                    end -= 1
            else:
                end -= 1
        
        print(start, end)

    arr[0], arr[start] = arr[start], pivot
    quick_sort(arr, 0, start)
    quick_sort(arr, start + 1, end_ori)

def heap_sort(arr: list[float]) -> None:
    pass

arr1 = [random.random() for _ in range(10)]
print(arr1)
quick_sort(arr1, 0, len(arr1) - 1)
print(arr1)