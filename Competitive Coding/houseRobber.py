"""
(https://leetcode.com/problems/house-robber/)

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each
of them is that adjacent houses have security system connected and it will automatically contact the
police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

"""
from typing import List

#just passed 39 test cases
"""class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        odd_sum = 0
        even_sum = 0
        for i,v in enumerate(nums):
            if (i%2==0):
                even_sum += v
            else:
                odd_sum += v
        if(odd_sum<even_sum):
            return even_sum
        else:
            return odd_sum
"""
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0 :
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        acc = [0] * n
        
        acc[0] = nums[0]
        acc[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            acc[i] = max(nums[i] + acc[i-2], acc[i-1])
            
        return acc[-1]
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        len_arr = len(nums)
        max_val_two_houses_ago = 0
        max_val_one_house_ago = 0

        for i in range(len_arr):
            cur_house_val = nums[i]
            rob_cur_house = max_val_two_houses_ago + cur_house_val
            skip_cur_house = max_val_one_house_ago
            max_val_two_houses_ago = max_val_one_house_ago
            max_val_one_house_ago = max(rob_cur_house, skip_cur_house)
        return max(max_val_two_houses_ago, max_val_one_house_ago)

nums = [2,1,1,2]

print(Solution.rob(self=Solution,nums=nums))