from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = defaultdict(int)
        # if len()
        for i in nums1:
            s[i] +=1
        ans = []
        for i in nums2:
            if s[i]>0:
                ans.append(i)
                s[i] -=1

        return ans