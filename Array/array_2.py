def two_sum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return arr[i],arr[j]
    
arr=[4,5,2,2,5,2,5,6]
target=9
result=two_sum(arr,target)
print(result)