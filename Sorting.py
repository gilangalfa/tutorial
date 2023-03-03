from random import randint

def partition(o, n, e):
    pivot = o[e]
    index = n
    now = n
    while (now < e) :
        if o[now] <= pivot:
            o[index],o[now]=o[now],o[index]
            index += 1
        now += 1
    o[index],o[e] = o[e],o[index]
    return index

def quicksort(t, w, o):
  if w < o:
    index = partition(t, w, o)
    quicksort(t, w, index-1)
    quicksort(t, index+1, o)
    return t

angka = [randint(1, 20) for i in range(10)]
print("Sebelum disort : ", angka)

akhir = quicksort(angka,0,len(angka)-1)
print("Setelah disort : ",akhir)