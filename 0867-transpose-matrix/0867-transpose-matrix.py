class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        c=len(matrix[0])
        r=len(matrix)
        m=[]
        for i in range(c):
            p=[]
            m.append(p)
            for j in range(r):
                p.append(matrix[j][i])
             
        return m
        