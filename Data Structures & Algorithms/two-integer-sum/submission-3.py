class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_dict = {}

        for i in range(n):
            if nums[i] in nums_dict:
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]] = [i]

        for i in range(n):
            num = nums[i]
            res = target - num
            if res in nums_dict:
                if len(nums_dict[res]) == 2:
                    return nums_dict[res]
                else:
                    if i != nums_dict[res][0]:
                        return [i, nums_dict[res][0]]