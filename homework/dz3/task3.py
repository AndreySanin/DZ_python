# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def difference(my_list):
    if len(my_list)==0:
        return "Пустой список"
    else:
        max=abs(my_list[0]%1)
        min=abs(my_list[0]%1)
        for i in my_list:
            fraction=abs(i%1)
            if fraction!=0:
                if fraction>max:
                    max=fraction
                elif fraction<min:
                    min=fraction
        return max-min

my_list=[1.1, 1.2, 3.1, 5, 10.01] # ввод списка
print(difference(my_list))