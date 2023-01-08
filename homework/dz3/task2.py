# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def pairs_multiplication(my_list):
    if len(my_list)==0:
        return "Пустой список"
    else:
        i=1
        list_of_pairs=[]
        while i<len(my_list)/2+1:
            list_of_pairs.append(my_list[i-1]*my_list[-i])
            i+=1
        return list_of_pairs

my_list=[2, 3, 4, 5, 6] # ввод списка
print(pairs_multiplication(my_list))