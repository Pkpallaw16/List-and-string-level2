class Solution(object):
    def check_Freq_Maj2(self, arr, val):
        count = 0
        for ele in arr:
            if ele == val:
                count += 1
        return float(count) > len(arr) / 3

    def majorityElement(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        val1 = arr[0]
        count1 = 1
        val2 = arr[0]
        count2 = 0
        for i in range(1, len(arr)):
            if arr[i] == val1:
                count1 += 1
            elif arr[i] == val2:
                count2 += 1
            else:
                if count1 == 0:
                    val1 = arr[i]
                    count1 = 1
                elif count2 == 0:
                    val2 = arr[i]
                    count2 = 1
                else:
                    count1 -= 1
                    count2 -= 1

        lis = []
        check1 = self.check_Freq_Maj2(arr, val1)
        if check1:
            lis.append(val1)

        check2 = self.check_Freq_Maj2(arr, val2)
        if check2:
            lis.append(val2)
        return lis

