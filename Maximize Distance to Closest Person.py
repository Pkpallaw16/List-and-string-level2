class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maxdistance=0
        prev_one_index=-1
        count=0
        for i in range(len(seats)):
            if seats[i]==0:
                count+=1
                if i==len(seats)-1:
                    maxdistance = max(maxdistance, count)
            elif seats[i]==1:
                if prev_one_index==-1:
                    maxdistance=max(maxdistance,count)
                    prev_one_index=i
                    count=0
                else:
                    if count%2==0:
                        s=int(count/2)
                    else:
                        s=int(count/2)+1
                    maxdistance = max(maxdistance,s)
                    count = 0
        return maxdistance