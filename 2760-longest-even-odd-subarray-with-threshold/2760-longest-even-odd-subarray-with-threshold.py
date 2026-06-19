class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        o = []
        ans = 0
        for i in range(r):
            if nums[i] > threshold:
                o = []
                l = 0
                continue
            if l == 0:
                if nums[i] % 2 == 0:
                    o = [nums[i]]
                    l = 1
            else:
                if nums[i-1] % 2 != nums[i] % 2:
                    o.append(nums[i])
                    l += 1
                else:
                    if nums[i] % 2 == 0:
                        o = [nums[i]]
                        l = 1
                    else:
                        o = []
                        l = 0

            ans = max(ans, l)
        return ans