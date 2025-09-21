arr=[1,2,3,4,5,6]
even=[]
for i in range(len(arr)):
    if arr[i]%2==0:
        even.append(arr[i])
print(even)