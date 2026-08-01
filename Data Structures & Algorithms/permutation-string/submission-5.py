class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict={}
        for w in s1:s1_dict[w] = s1_dict.get(w,0) + 1

        s2_window_dict={}
        ptr_left_s2=0

        for ptr_right_s2 in range(len(s2)):
            next_alphabet = s2[ptr_right_s2]
            s2_window_dict[next_alphabet] = s2_window_dict.get(next_alphabet,0) + 1

            while ptr_right_s2+1-ptr_left_s2 > len(s1):
                s2_window_dict[ s2[ptr_left_s2] ] -=1
                if s2_window_dict[ s2[ptr_left_s2] ] == 0:
                   del s2_window_dict[ s2[ptr_left_s2] ] 
                ptr_left_s2 += 1


            if s1_dict == s2_window_dict:
                return True
        
        return False
