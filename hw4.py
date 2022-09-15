# 1 Вычислить число π c заданной точностью d
# *Пример:* - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
def my_pi(d: int) -> float:
    pi, sign, m = 3, 1, 2
    while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-d-1):
        pi = pi + sign*4/(m**3+3*m**2+2*m)
        sign = -1*sign
        m = m+2
    return round((pi + (pi + sign*4/(m**3+3*m**2+2*m)))/2, d)

d = int(input('Введите точность определения числа ПИ (количество знаков после запятой): '))
pi = my_pi(d)
print(f'С точностью {d=}, число {pi=}; ')

# 2 Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
num = int(input("Введите число: "))
i = 2 # первое простое число
a = []
b = num
while i <= num:
    if num % i == 0:
        a.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {b} приведены в списке: {a}")

# 3 Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
x = list(map(int, input("Задайте последовательность чисел через пробел:\n").split()))
print(f"список чисел: {x}")
y = []
[y.append(i) for i in x if i not in y]
print(f"Список из неповторяющихся элементов: {y}")

# 4 Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
import itertools

k = randint(2, 7)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')

ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('4_hw.txt', 'w') as data:
    data.write(polynom1)
    
# 5 Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.