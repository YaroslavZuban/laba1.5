from ctypes import *

# Загружаем библиотеку
adder = CDLL('./adder.so')

# Находим сумму целых чисел
res_int = adder.add_int(4,5)
print("Сумма 4 и 5 = " + str(res_int))
