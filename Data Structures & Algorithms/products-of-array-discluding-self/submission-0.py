class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n

        #multiply left side
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            
        #multiply right
        for i in range(0,n-1):
             suffix[-(i + 2)] = suffix[-(i + 1)] * nums[-(i + 1)]

        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer