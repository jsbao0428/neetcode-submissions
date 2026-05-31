class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[0] = max(dp[0-1], dp[0-2] + nums[0])


        n = len(nums)
        if rob first, skip last
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n-1):
                pass
        if rob last

        """
        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])

        
        # build helper function
        def rob(nums, start, end):
            n = end-start
            dp = [0] * n
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start+1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[start+i])
            return dp[-1]

        # if rob first, skip last

        # if rob last, skip first

        return max(rob(nums, 0, n-1), rob(nums, 1, n))