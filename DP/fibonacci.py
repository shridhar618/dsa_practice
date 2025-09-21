def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Create DP array
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    
    # Fill the dp table
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


# Example
n = 10
print(f"The {n}th Fibonacci number is:", fibonacci(n))
