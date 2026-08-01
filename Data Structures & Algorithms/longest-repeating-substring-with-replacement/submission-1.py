class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window_dict=dict()
        ptr_left=0
        max_length_repeating_char=0
        for ptr_right in range(len(s)):
            window_dict[s[ptr_right]]=window_dict.get(s[ptr_right], 0) + 1
            window_length=sum(window_dict.values())

            while window_length - max(window_dict.values()) > k:
                window_dict[s[ptr_left]]-=1
                ptr_left+=1
                window_length-=1

            if window_length > max_length_repeating_char:
                max_length_repeating_char = window_length
        
        return max_length_repeating_char
        