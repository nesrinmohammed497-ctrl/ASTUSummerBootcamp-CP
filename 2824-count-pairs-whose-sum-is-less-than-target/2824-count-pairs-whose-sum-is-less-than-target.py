class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r=0
        l=len(nums)-1
        p=0
        nums.sort()
        while r<l:
            if nums[r] + nums[l]<target:
                p+=l-r
                r+=1
            else:
                l-=1
        return p
        