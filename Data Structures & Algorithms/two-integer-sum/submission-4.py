class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_dict = {}

        for i in range(n):
            res = target - nums[i]
            if res in nums_dict:
                return [nums_dict[res],i]
            nums_dict[nums[i]] = i