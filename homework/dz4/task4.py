# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def koef_list(k):
    lst=[]
    for i in range(k):
        lst.append(random.randint(0, 100))
    return lst
    
def polynomial(k,koeffs):
    polynom=[]
    for i in koeffs:
        if i!=0:
            polynom.append(f"{str(i)}x^{str(k)}+")
            k-=1
        else:
            k-=1
    polynom.append(str(random.randint(0, 100)))
   
    return ''.join(polynom)

k=int(input("Задайте натуральную степень k: "))
koeffs=koef_list(k)
result=polynomial(k, koeffs)
data = open('file.txt', 'w')
data.writelines(result)
data.close()