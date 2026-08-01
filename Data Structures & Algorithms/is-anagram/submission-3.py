class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        for ch in s:
            dict_s[ch] = 1 + dict_s.get(ch, 0)
        
        for ch in t:
            if ch not in dict_s:
                return False
            dict_s[ch] -= 1
            if dict_s[ch] < 0:  
                return False
        
        for _, num in dict_s.items():
            if num != 0:
                return False
        
        return True
