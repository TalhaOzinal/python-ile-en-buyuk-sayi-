
import random
import time

def enBuyukBruteforce(arr):
    maxSayi = arr[0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                maxSayi = arr[i]
    return maxSayi

arr = [random.randint(1, 100000) for i in range(10000)]

baslangic = time.time()
maxSayi = enBuyukBruteforce(arr)
bitis = time.time()

print("En büyük sayı: ", maxSayi)
print("Süre: ", bitis - baslangic, " saniye")

