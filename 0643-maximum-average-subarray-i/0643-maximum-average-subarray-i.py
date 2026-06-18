class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        w = sum(nums[:k])
        max_sum = w
        for i in range(k, len(nums)):
            w += nums[i] - nums[i - k]
            max_sum = max(max_sum, w)
        return max_sum /float(k) 
        