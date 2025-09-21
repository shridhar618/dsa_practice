def index(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
        
arr=[10,20,30]
target=30
result=index(arr, target)
print(result)