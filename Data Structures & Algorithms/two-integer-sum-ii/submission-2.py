class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr_left=0
        ptr_right=len(numbers)-1

        while ptr_left < ptr_right:
            if numbers[ptr_left] + numbers[ptr_right] == target:
                return [ptr_left+1,ptr_right+1]
            elif numbers[ptr_left] + numbers[ptr_right] > target:
                ptr_right-=1
            elif numbers[ptr_left] + numbers[ptr_right] < target:
                ptr_left+=1