class Solution:
    
    def dfs(self, nums):
        if len(self.permutation) == len(nums):
            self.results.append(self.permutation.copy())
            return

        for i in range(len(nums)):
            if nums[i] in self.permutation:
                continue

            self.permutation.append(nums[i])
            self.dfs(nums)
            self.permutation.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutation = []
        self.results = []
        self.dfs(nums)

        return self.results