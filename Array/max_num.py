num=[5,10,15,10]
max_num=num[0]
for i in range(len(num)):
    if num[i]>max_num:
        max_num=num[i]
print(max_num)