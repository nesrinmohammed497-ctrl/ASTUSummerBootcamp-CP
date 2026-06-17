class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        o = {}
        key = 0
        for i in nums:
            o[i] = o.get(i, 0) + 1
        for i in o:
            if i + 1 in o:
                key = max(key, o[i] + o[i + 1])

        return key
        