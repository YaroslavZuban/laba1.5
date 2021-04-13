import random
import time

startT = time.time()
mas = []
size = 100
for i in range(0, 100):
    mas.append(random.randint(1, 100))
sort_mas = sorted(mas)
print('Время работы программы: ', sort_mas[0], '%s sec' % (time.time() - startT))

print("\nВнимание программа на С++\n")

# Zadanie2
from ctypes import *

# Загружаем библиотеку
startTi = time.time()
sort = CDLL('./sort.so')
sort.bubbleSort.restype = c_int
# Указываем, что функция принимает аргумент int
sort.bubbleSort.argtypes = [c_int,]
print('Время работы программы C++: ', sort.bubbleSort(100), '%s sec' % (time.time() - startTi))
