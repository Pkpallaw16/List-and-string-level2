def First_Missing_Positive(nums):
    one=False
    for i in range(len(nums)):
        if nums[i]==1:
            one=True
        if nums[i]<1 or len(nums)<nums[i]:
            nums[i]=1
    if one==False:
        return 1
    for i in range(len(nums)):
        val=abs(nums[i])
        indx=val-1
        nums[indx]=-abs(nums[indx])
    for i in range(len(nums)):
        if nums[i]>0:
            return i+1
    return len(nums)+1