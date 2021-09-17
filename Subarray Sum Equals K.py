class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = {}
        sum = 0
        count = 0
        prefix_sum[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in prefix_sum:
                count += prefix_sum[sum - k]
                if sum in prefix_sum:
                    prefix_sum[sum] += 1
                else:
                    prefix_sum[sum] = 1

            else:
                if sum in prefix_sum:
                    prefix_sum[sum] += 1
                else:
                    prefix_sum[sum] = 1
        return count