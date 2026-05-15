def binary_search(nums, target):
    n=len(nums)-1
    left=0
    right=n-1
    
    while left<=right:
        mid=(left+right)//2
        if target<nums[mid]:
            right=mid-1
        elif target>nums[mid]:
            left=mid+1
        else:
            return mid
        
    return -1

nums=[2,3,6,7,8,9]
target=7
result=binary_search(nums, target)
print(result)