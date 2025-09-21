def first_recurring_no(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):   
            if nums[i] == nums[j]:
                return nums[i]
    return None                            

nums = [2, 5, 3, 5, 2]
print(first_recurring_no(nums))  
