class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        left = 0
        right = 2
        count=0
        n=len(colors)-1
        while right < len(colors) :
            if colors [left] != colors [left +1] and colors[right] != colors [left +1]:
                count+=1
            left +=1
            right +=1
        if colors [0] != colors [1] and colors[n] != colors [0]:
            count+=1
        if colors [n] != colors [0] and colors[n] != colors [n - 1]:
            count+=1
        return count


        