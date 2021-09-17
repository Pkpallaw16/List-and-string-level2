class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_ele = None
        count = 0
        for i in range(len(nums)):
            if maj_ele == None:
                maj_ele = nums[i]
                count += 1
            elif maj_ele == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    maj_ele = None
        return maj_ele
    def majorityElement_2nd(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_ele = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if maj_ele == nums[i]:
                count += 1
            elif count>0:
                count -= 1
            else:
                if count == 0:
                    maj_ele = nums[i]
                    count=1
        return maj_ele
arr=[3,2,3]
s=Solution()
print(s.majorityElement(arr))
print(s.majorityElement_2nd(arr))