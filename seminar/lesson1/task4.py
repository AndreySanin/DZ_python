# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру 
# дробной части числа.
    
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

num = float(input("Введите дробное число: "))
if num % 1 == 0:
    print("нет")
else:
    print(f"{num} -> {int(abs(num)*10%10)}")

# Другое решение:

print("Другое решение")

num = input('enter number: ')
if '.' in num:
    index_num = num.find('.')+1
    print(num[index_num])
elif ',' in num:
    index_num = num.find(',')+1
    print(num[index_num])
else:
    print('no')