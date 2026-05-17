def max_num_subarray(nums, k):
    window_sum = 0
    for i in range(k):
        window_sum+=nums[i]
    
    max_sum=window_sum
    
    for i in range(k,len(nums)):
        window_sum=window_sum-nums[i-k]
        window_sum=window_sum+nums[i]
        
        max_sum=max(max_sum, window_sum)
        
    return max_sum


nums=[3,2,5,3,8,4,2,1]
k=3
result=max_num_subarray(nums,k)
print(result)
    
        