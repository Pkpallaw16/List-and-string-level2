import sys
def Maximum_Subarray(nums):
    csum=0
    osum=-sys.maxsize
    start=0
    end=0
    for i in range(len(nums)):
        if csum<0:
            csum=nums[i]
            start=i
        else:
            csum+=nums[i]
        if osum<csum:
            osum=csum
            end=i
    for i in range(start,end+1):
        print(nums[i],end=" ")
    return osum
print(Maximum_Subarray([-2,1,-3,4,-1,2,1,-15,4]))