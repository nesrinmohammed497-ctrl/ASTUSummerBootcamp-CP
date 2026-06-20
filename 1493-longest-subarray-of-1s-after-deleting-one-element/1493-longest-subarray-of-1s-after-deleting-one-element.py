class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        w = 0     
        f = 0      # number of zeros in window
        o = 0      # answer
        for i in range(len(nums)):
            if nums[i] == 0:
                f += 1
            while f > 1:
                if nums[w] == 0:
                    f -= 1
                w += 1
            o = max(o, i - w + 1)
        return o - 1