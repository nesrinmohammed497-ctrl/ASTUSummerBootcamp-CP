class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        p =0
        lm=0
        rm=0
        while l<r:
            if height[r]>height[l]:
                if height[l] >= lm:
                    lm = height[l]
                else:
                    p += lm - height[l]
                l += 1
            else:
                if height[r] >= rm:
                    rm = height[r]
                else:
                    p += rm - height[r]
                r -= 1
        return p