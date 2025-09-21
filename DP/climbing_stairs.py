def climbStairs(n):
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # DP array
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    
    # Fill dp table
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Example
n = 5
print(f"Number of ways to climb {n} stairs:", climbStairs(n))
