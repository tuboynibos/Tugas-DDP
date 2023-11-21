def ganjil(n):
    n += 1
    for i in range(1, n, 2):
        print(i, end=",")
ganjil(100)