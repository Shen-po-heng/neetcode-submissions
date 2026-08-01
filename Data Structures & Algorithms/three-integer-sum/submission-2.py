class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        return_list=[]

        for i in range(len(sorted_nums)-2):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            ptr_left = i+1
            ptr_right = len(sorted_nums)-1

            while ptr_left < ptr_right:
                sum_of_the_other_two=sorted_nums[ptr_left]+sorted_nums[ptr_right]
                if -sorted_nums[i] == sum_of_the_other_two:
                    return_list.append([sorted_nums[i],sorted_nums[ptr_left],sorted_nums[ptr_right]])
                    ptr_left += 1
                    ptr_right -= 1

                    # 跳過重複的左側數字
                    while (
                        ptr_left < ptr_right
                        and sorted_nums[ptr_left] == sorted_nums[ptr_left - 1]
                    ):
                        ptr_left += 1

                    # 跳過重複的右側數字
                    while (
                        ptr_left < ptr_right
                        and sorted_nums[ptr_right] == sorted_nums[ptr_right + 1]
                    ):
                        ptr_right -= 1
                elif -sorted_nums[i] > sum_of_the_other_two:
                    ptr_left+=1
                elif -sorted_nums[i] < sum_of_the_other_two:
                    ptr_right-=1
                
        return return_list