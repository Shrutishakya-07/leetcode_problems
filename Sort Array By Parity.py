class Solution(object):
    def sortArrayByParity(self, nums):
        l1 = []
        l2 = []
        ans= []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                l1.append(nums[i])
            elif nums[i]%2 != 0:
                l2.append(nums[i])
        ans.extend(l1)
        ans.extend(l2)
        return ans
