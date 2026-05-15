# def first_recurring_no(nums):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):   
#             if nums[i] == nums[j]:
#                 return nums[i]
#     return None                            

# nums = [2, 5, 3, 5, 2]
# print(first_recurring_no(nums))  



# def first_recurring_no_2(nums):
#     left=0
#     right=len(nums)-1
    
#     for i in range(len(nums)):
#         if nums[left]==nums[right]:
#             return nums[left]



def first_recurring_no_2(nums):
    freq={}
    for num in nums:
        if num in freq:
            return num
        freq[num]=1
    
nums=[2,4,3,5,2,3,8,7]
result=first_recurring_no_2(nums)
print(result)
