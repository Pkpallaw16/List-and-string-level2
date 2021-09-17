def two_sum(arr,st,end,target):
    left=st
    right=end
    res=[]
    while left<right:
        if left!=st and arr[left]==arr[left-1]:
            left+=1
            continue
        sum1=arr[left]+arr[right]
        if sum1==target:
            subres=[]
            subres.append(arr[left])
            subres.append(arr[right])
            res.append(subres)
            left+=1
            right-=1
        elif sum1>target:
            right-=1
        else:
            left+=1
    return res
def Three_sum(nums,target):
    nums.sort()
    res=[]
    for i in range(len(nums)-2):
        val1=nums[i]
        small_target=target-val1
        subres=two_sum(nums,i+1,len(nums)-1,small_target)
        for lis in subres:
            lis.append(val1)
            res.append(lis)
    return res
print(Three_sum([-1,0,1,2,-1,-4],0))