class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_num=0
        right_num=len(nums)-1

        while left_num <= right_num:
            target_index = left_num + (right_num-left_num)//2
            if nums[target_index] == target:
                return target_index
            elif nums[target_index] >target:
                right_num=target_index-1
            else:
                left_num=target_index+1
        
        return -1
