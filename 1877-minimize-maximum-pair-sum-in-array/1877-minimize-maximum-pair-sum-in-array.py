class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        p=[]
        r=0
        l=len(nums)-1
        while r<l :
            p.append(nums[r]+nums[l])
            r+=1
            l-=1
        return max(p)
        