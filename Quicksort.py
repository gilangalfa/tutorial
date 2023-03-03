import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr)-1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [random.randint(0, 10) for _ in range(10)]
print("Sebelum di-sort: ", arr)
arr_sorted = quicksort(arr)
print("Setelah di-sort: ", arr_sorted)