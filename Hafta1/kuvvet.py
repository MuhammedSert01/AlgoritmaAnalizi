def kuvvet(a,b):
    sayi = 1
    while b:
        if b & 1:
            sayi *= a
        b >>= 1
        a = a * a
    return sayi
print(kuvvet(2, 4))
