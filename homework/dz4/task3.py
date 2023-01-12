# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

def str_to_list_of_nums(strng):
    nums=[]
    for i in strng:
        if i!=" ":
            nums.append(int(i))
    return nums

def not_repeated_nums(nums):
    lst=[]
    for i in nums:
        if i not in lst:
            lst.append(i)
    return lst

nums=input("Введите числа через пробел: ")
print(not_repeated_nums(str_to_list_of_nums(nums)))