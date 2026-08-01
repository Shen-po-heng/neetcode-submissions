class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        count = 0

        for n in nums:
            nums_dict[n] = count
            count += 1


        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums_dict and nums_dict[complement] != i:
                return [i, nums_dict[complement]]

        return []