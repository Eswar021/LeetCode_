class Solution(object):
    def missingNumber(self, nums):
        return list(set(range(0,len(nums)+1)).difference(set(nums)))[0]