#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        while(len(str(n)) > 1):

            summ = 0
            for i in str(n):
                summ += int(i) ** 2
            n = summ
        if n == 1 or n == 7:
            return True
        else:
            return False      
