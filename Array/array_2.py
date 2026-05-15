# def two_sum(arr,target):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==target:
#                 return arr[i],arr[j]
    
# arr=[4,5,2,2,5,2,5,6]
# target=9
# result=two_sum(arr,target)
# print(result)


#two sum 2
def two_sum_2(arr,target):
    left=0
    right=len(arr)-1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
            
            
arr=[1,2,3,4,5,6,7,8,9]
target=17
result=two_sum_2(arr, target)
print(result)
        