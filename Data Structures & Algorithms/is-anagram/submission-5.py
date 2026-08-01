class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        for word in s:
            if word not in s_dict:
                s_dict[word]=1
            else:
                s_dict[word]+=1
        for word in t:
            if word not in s_dict:
                return False
            else:
                s_dict[word]-=1
        for word in s_dict:
            if s_dict[word]!=0:
                return False
        return True