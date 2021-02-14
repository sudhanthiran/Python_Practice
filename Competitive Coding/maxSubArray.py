from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        sum_nums = nums[0]
        temp = nums[0]
        for i in nums[1:]:
            if (temp + i > i):
                temp = temp + i
            else:
                temp = i
            if (sum_nums < temp):
                sum_nums = temp

        return sum_nums

nums = [-2,1,-3,4,-1,2,1,-5,4]

print(Solution.maxSubArray(self=Solution,nums=nums))