class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        s=[]
        o=0
        for char in str(nums):
            s.append(char)
        if str(digit) in s:
                 o+=1
        return s.count(str(digit)) 
        
        

        