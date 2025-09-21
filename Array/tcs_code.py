def tcs(arr):
    for i in range(len(arr)):
        if arr[i]>0:
            arr[i]=1
        elif arr[i]<0:
            arr[i]=arr[i]*arr[i]
        else:
            print("wrong input")
    return arr

arr=[4,-4,1,1,5,-6,-1]
result=tcs(arr)
print(result)
            