class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set=set()
        max_length=0
        ptr_left=0
        

        for ptr_right in range (len(s)) :
            while s[ptr_right] in s_set:
                s_set.remove(s[ptr_left])
                ptr_left += 1
            s_set.add(s[ptr_right])

            if len(s_set)>max_length:
                max_length=len(s_set)
        return max_length
        
