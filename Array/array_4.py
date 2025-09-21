def gpt(arr):
    if len(arr)==1:
            return True
    for i in range(len(arr)):
        
        if arr[i]>arr[i+1]:
            return False
    return True
        
        
        
arr=[1,2,3,5,4]
result=gpt(arr)
print(result)