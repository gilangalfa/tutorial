import os
os.system("cls")

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    elif right:
        result += right
    return result

angka = [2, 1, 9, 4, 6]

hasil = mergeSort(angka)

print(hasil)

#CONTOH RINGKAS
# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left = mergeSort(arr[:mid])
#     right = mergeSort(arr[mid:])

#     return merge(left, right)

# def merge(left, right):
#     result = []

#     i = j = 0

#     while i < len(left) and j < len(right):
#         if isinstance(left[i], str) and isinstance(right[j], str):
#             if left[i] < right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1

#         elif isinstance(left[i]):
#             result.append(left[i])
#         else:
#             if left[i] < right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1

#     result.extend(left[i:])
#     result.extend(right[:j])

#     return result

# def merge(arr):
#     for i in arr:
#         penampungan.append(i)

# penampungan = []

# listacak = [1, 2, "a", "11", 5]

# print(mergeSort(listacak))