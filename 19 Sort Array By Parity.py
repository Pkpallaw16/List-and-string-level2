def Sort_Array_By_Parity(nums):
    j=0
    i=0
    while i <len(nums):
        if nums[i]%2!=0:
            i+=1
        else:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
    return nums       