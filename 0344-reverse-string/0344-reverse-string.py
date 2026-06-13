class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s_rev=[]
        for i in range (len(s)-1,-1,-1):
            s_rev.append(s[i])
        for i in range (len(s)):
            s[i]=s_rev[i]
        return s