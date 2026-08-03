class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()
        child=0
        cookie=0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child+=1
            cookie+=1
        return child
        