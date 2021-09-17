class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0 for i in range(len(nums))]
        i=0
        j=len(nums)-1
        k=len(nums)-1
        while i<=j:
            if nums[j]*nums[j]>nums[i]*nums[i]:
                res[k]=nums[j]*nums[j]
                j-=1
            else:
                res[k]=nums[i]*nums[i]
                i+=1
            k-=1    
        return res