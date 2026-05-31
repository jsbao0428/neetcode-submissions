class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i], nums[i] 0:i 之間 最長的  
        # base case dp[0] = 0
        # base case dp 最小就是 自己 = 1
        
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

                
