class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        p=0
        for i in range(0,len(s)-1):
            k=i-1
            p+=abs(ord(s[i])-ord(s[i+1]))
        return p
       
        
