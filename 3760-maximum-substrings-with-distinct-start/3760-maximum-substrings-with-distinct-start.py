class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        u=[]
        for i in range(len(s)):
            if s[i] not in u:
                u.append(s[i])
        return len(u)
        
        