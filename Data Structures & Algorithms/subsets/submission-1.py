class Solution:

    def dfs(self, i:int, nums: List[int]):
        if i ==len(nums):
            self.results.append(self.subset.copy())
            return
        self.subset.append(nums[i])
        self.dfs(i + 1, nums)
        self.subset.pop()
        self.dfs(i + 1, nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subset = []
        self.results = []
        self.dfs(0,nums)
        return self.results