import random
import time


def enBuyukSayi(arr):
    maxSayi = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxSayi:
            maxSayi = arr[i]
    return maxSayi


arr = [random.randint(1, 100000) for i in range(10000)]

baslangic = time.time()
maxSayi = enBuyukSayi(arr)
bitis = time.time()

print("En büyük sayı: ", maxSayi)
print("Süre: ", bitis - baslangic, " saniye")
