class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len (strs)
        used = [False]*n
        cnts = [Counter(s) for s in strs]
        output = []

        for i in range(n):
            if used[i] == True:
                continue
            group = [strs[i]]
            used[i] = True
            for j in range(i+1, n):
               if not used[j] and cnts[i] == cnts[j]:
                    group.append(strs[j])
                    used[j] = True
            output.append(group)
        return output