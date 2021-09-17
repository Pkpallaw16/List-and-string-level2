import sys
def Partition_Array_Into_Disjoint_Intervals(nums):
    rightmin=[0 for i in range(len(nums))]
    n=len(nums)
    rightmin[n-1]=nums[n-1]
    for i in range(n-2,-1,-1):
        rightmin[i]=min(nums[i],rightmin[i+1])
    leftmax= -sys.maxsize
    ans=0
    for i in range(n-1):
        leftmax=max(leftmax,nums[i])
        if leftmax<=rightmin[i+1]:
            ans=i
        break
    return i+1

def Partition_Array_Into_Disjoint_Intervals_2nd(nums):
    leftmax=nums[0]
    maxIn_run=nums[0]
    ans=0
    for i in range(len(nums)):
        if nums[i]>maxIn_run:
            maxIn_run=nums[i]
        elif nums[i]<leftmax:
            ans=i
            leftmax=maxIn_run
    return ans+1