class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums_dict:
                return [nums_dict[complement], i]
            nums_dict[n] = i

        return []