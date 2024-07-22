#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = 0
        for i in nums:
            if count == 0:
                candidate = i
            count += (1 if i == candidate else -1)
        if nums.count(candidate) > len(nums) / 2:
            return candidate



        



# @lc code=end

