class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        ans = 0
        min_i = -1
        max_i = -1
        bad_i = -1
        
        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                bad_i = i
            if x == minK:
                min_i = i
            if x == maxK:
                max_i = i
                
            ans += max(0, min(min_i, max_i) - bad_i)
                
        return ans
