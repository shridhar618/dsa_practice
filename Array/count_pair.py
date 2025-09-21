def count_pair(num, k):
    count=0
    for i in range(len(num)):
        for j in range(i, len(num)):
            if num[j]-num[i]==k:
                count+=1
    return count

num=[1,3,5]
k=2
print(count_pair(num,k))