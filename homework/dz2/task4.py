# 4   Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#     Найдите произведение элементов на указанных позициях. 

N=int(input("Введите значение N: "))
my_list=[i for i in range(-N,N+1)]
print(f"Список из N элементов: {my_list}")
positions=[2,4,6]
print(f"Позиции: {positions}")
mult=1
for i in positions:
    mult=mult*my_list[i]
print(f"Произведение элементов на указанных позициях: {mult}")
