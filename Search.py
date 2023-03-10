var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
print(var)

def Search(data):
    for i in range(len(var)):
        if isinstance(var[i], str) and var[i] == data:
            return i
        elif isinstance(var[i], list) and data in var[i]:
            return (i, var[i].index(data))
    return None

while True:
    Find = input("Masukkan nama : ")
    result = Search(Find)
    if result is None:
        print(Find, "Tidak ada dalam list.")
    elif isinstance(result, int):
        print(Find, "Ditemukan pada indeks ke", result)
    else:
        print(f"{Find} ditemukan pada indeks ke-{result[0]} pada list dan pada kolom ke", {result[1]})
