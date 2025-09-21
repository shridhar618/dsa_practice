def maxSubArray(nums):
    # Initialize current sum and max sum
    current_sum = nums[0]
    max_sum = nums[0]
    
    # Traverse array
    for i in range(1, len(nums)):
        # Either extend the current subarray OR start a new one
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example
nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Maximum subarray sum:", maxSubArray(nums))
