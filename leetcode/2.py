l1,l2 = [2,4,3],[5,6,4]
num=0
for i in range(min(len(l1),len(l2))):
    num=num+(l1[i]+l2[i])*10**i
my_list=list(str(num))
for i in range((len(my_list)//2)-1):
    temp=my_list[i]
    my_list[i]=my_list[-i]
    my_list[-i]=temp 
print(my_list)
