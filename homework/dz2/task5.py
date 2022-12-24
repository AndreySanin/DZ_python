# 5 Реализуйте алгоритм перемешивания списка.

import random


my_list=[1,"siuuuu",3,"h,yu,rf",5]
new_list=[]
for i in range(len(my_list)):
    j=random.randint(0,len(my_list)-1)
    new_list.append(my_list[j])
    my_list.pop(j)
print(new_list)