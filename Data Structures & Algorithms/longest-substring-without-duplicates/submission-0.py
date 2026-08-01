class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0;
        elif len(s) == 1:
            return 1;

        s_set=set()
        max_length=1 #intial value
        ptr_left=0
        ptr_right=1

        s_set.add(s[ptr_left])

        while ptr_right < len(s) :
            if s[ptr_right] not in s_set:
                s_set.add(s[ptr_right])
            else:
                while ptr_left < ptr_right:
                    if s[ptr_left] != s[ptr_right]:
                        s_set.remove(s[ptr_left])
                        ptr_left+=1
                    else: #s[ptr_left] == s[ptr_right]
                        s_set.remove(s[ptr_left])
                        ptr_left += 1
                        s_set.add(s[ptr_right])
                        break
            ptr_right+=1
            if len(s_set)>max_length:
                max_length=len(s_set)
        
        return max_length
        
