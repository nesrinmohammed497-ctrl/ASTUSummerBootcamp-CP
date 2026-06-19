class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        o=[]
        p=[]
        for i in range (len(score)):
            o.append(score[i][k])
        o.sort()
        for i in range(len(score)):
            for j in range(len(score)):
                if o[i] == score[j][k]:
                    p.insert(0,score[j])
        return p
                






        