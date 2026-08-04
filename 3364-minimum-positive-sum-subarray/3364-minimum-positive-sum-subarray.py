class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        m = float('inf')
        for size in range(l, r + 1):
            if size > n:
                break
            s = sum(nums[:size])
            if s > 0:
                m = min(m, s)
            for i in range(size, n):
                s += nums[i] - nums[i - size]
                if s > 0:
                    m = min(m, s)
        return m if m != float('inf') else -1

        