import timeit
import random

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(R)
        merge_sort(L)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
        
    return arr

# вбудована функція sorted
def timesort(arr):
    return sorted(arr)

# функції тестування
def test_insertion_sort():
    arr = random.sample(range(1000), 1000)
    insertion_sort(arr)

def test_merge_sort():
    arr = random.sample(range(1000), 1000)
    merge_sort(arr)

def test_timsort():
    arr = random.sample(range(10000), 1000)
    timesort(arr)

# Заміри часу виконання
insertion_sort_time = timeit.timeit("test_insertion_sort()", globals=globals(), number=100)
merge_sort_time = timeit.timeit("test_merge_sort()", globals=globals(), number=100)
timsort_time = timeit.timeit("test_timsort()", globals=globals(), number=100)

print(f"Insertion sort: {insertion_sort_time} seconds")
print(f"Merge sort: {merge_sort_time} seconds")
print(f"Timsort: {timsort_time} seconds")