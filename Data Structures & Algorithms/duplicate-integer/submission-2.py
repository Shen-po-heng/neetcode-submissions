class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared_list = set()
        for num in nums:
            if num in appeared_list:
                return True
            else:
                appeared_list.add(num)
        return False