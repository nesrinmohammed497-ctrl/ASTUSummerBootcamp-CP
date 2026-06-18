class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less=[]
        great=[]
        mid=[]
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                mid.append(i)
            else:
                great.append(i)
        return less +mid + great
        
       

        