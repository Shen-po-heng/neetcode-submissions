class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strs_dict={}
        return_list=[]

        for val in strs:
            strs_dict.setdefault(tuple(sorted(val)), []).append(val)

        return list(strs_dict.values())