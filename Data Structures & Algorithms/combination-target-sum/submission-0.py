class Solution:
    def dfs (self, start:int , total:int , nums:List[int], target: int):
        if total == target:
            self.results.append(self.combination.copy())
        elif total > target:
            return
        else:
            for i in range(start, len(nums)):
                self.combination.append(nums[i])
                
                self.dfs(i,total + nums[i],nums,target)
                
                self.combination.pop()
                
            
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.combination = []
        self.results = []

        self.dfs(0,0,nums,target)

        return self.results