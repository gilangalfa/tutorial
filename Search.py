import math
def jump_search(arr,search):
    interval = int(math.sqrt(len(arr)))
    for i in range(0,len(arr),interval):
        if arr[i] >  search:
            chunk = i
            break
        if arr[i] ==  search:
            return i
    arr_ls = arr[chunk-interval:chunk]
    ind = [i for i,d in enumerate(arr_ls) if d==search]
    return chunk-interval+ind[0]
arr = [ i for i in range(1,200,15)]

res = jump_search(arr, 121)
print(res)