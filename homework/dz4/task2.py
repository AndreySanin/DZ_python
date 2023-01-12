# 2 Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def prime_factors(N):
    div=2
    dividers=[]
    while N!=1:
        if N%div==0:
            N=N/div
            dividers.append(div)
        else:
            div+=1
    return dividers

num=int(input("Задайте натуральное число N: "))
print(prime_factors(num))