class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], i+1):
                if num1 + num2 == target:
                    result.append(i)
                    result.append(j)
                    return result
