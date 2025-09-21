def nonRepeatingEle(nums):
    freq={}
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
            
    for num in freq:
        if freq[num]==1:
            return num
                
                
nums=[3,5,4,6,3,4]
result=nonRepeatingEle(nums)
print(result)
