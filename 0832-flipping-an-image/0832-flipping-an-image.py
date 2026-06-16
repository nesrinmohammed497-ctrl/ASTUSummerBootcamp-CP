class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        r=0
        l=len(image)
        for i in range(l):
            image[i].reverse()
            for j in range(l):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
            
        return image
            

        