class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s=re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        ptr_front = 0
        ptr_end = len(clean_s) - 1

        while ptr_front < ptr_end:
            if clean_s[ptr_front]==clean_s[ptr_end]:
                ptr_front += 1
                ptr_end -= 1
            else:
                return False
        return True