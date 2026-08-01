class Solution:

    def encode(self, strs: List[str]) -> str:
        return_str=""
        
        for word in strs:
            lenth=str(len(word))
            return_str += (lenth+"#"+word)
        return return_str
    
    def decode(self, s: str) -> List[str]:
        ptr=0
        return_list=[]
        
        while ptr < len(s):
            num=""
            count=0
            
            for char in s[ptr:]:
                if char != "#":
                    num+=char
                    count+=1
                else:
                    num = int(num)
                    break;
            word_start = ptr + count + 1
            word_end = word_start + num

            return_list.append(s[word_start:word_end])
            ptr = word_end
        return return_list
