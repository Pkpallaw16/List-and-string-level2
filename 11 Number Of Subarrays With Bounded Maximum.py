class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        prev_count = 0
        overall_count = 0
        i = 0
        j = 0
        while j < len(nums):
            if left <= nums[j] and nums[j] <=right:
                prev_count=j-i+1
                overall_count+=prev_count
            elif nums[j]<left:
                overall_count+=prev_count
            else:
                prev_count=0
                i=j+1
            j+=1
        return overall_count
