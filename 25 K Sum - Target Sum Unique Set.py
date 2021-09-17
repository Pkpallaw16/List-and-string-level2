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
def Ksum_helper(arr,target,si,k):
    if k==2:
        return two_sum(arr,si,len(arr)-1,target)
    n=len(arr)
    res=[]
    for i in range(si,n-(k-1)):
        if i!=si and arr[i]==arr[i-1]:
            continue
        val1=arr[i]
        targ=target-val1
        subres=Ksum_helper(arr,targ,i+1,k-1)
        for lis in subres:
            lis.append(val1)
            res.append(lis)
    return res
def K_sum(arr,target,k):
    arr.sort()
    res=Ksum_helper(arr,target,0,k)
    return res
print(K_sum([-1,0,1,2,-1,-4],0,3))