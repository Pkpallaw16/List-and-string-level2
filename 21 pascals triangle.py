class Solution(object):
    def getRow(self, rnum):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[]
        val=1
        for r in range(rnum+1):
            res.append(val)
            val=val*(rnum-r)/(r+1)
        return res