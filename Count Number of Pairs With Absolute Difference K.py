class Solution(object):
    def countKDifference(self, nums, k):
        count = 0
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], i+1):
                if num1 - num2 == k or num2 - num1 == k:
                    count += 1
        return count
