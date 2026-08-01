class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr_left = 0
        ptr_right = len(heights)-1
        max_area=0

        while ptr_left < ptr_right:
            area=(ptr_right-ptr_left)*min(heights[ptr_left],heights[ptr_right])
            if max_area < area:
                max_area = area
            if heights[ptr_left] < heights[ptr_right]:
                ptr_left +=1
            else:
                ptr_right-=1
            
        return max_area