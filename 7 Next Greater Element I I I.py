def dipIndex(lis):
    dip=-1
    i=len(lis)-1
    while i>0:
        if lis[i-1]<lis[i]:
            print("hi")
            dip=i-1
            return dip
        i-=1
    return dip
def ceilIndex(lis, indx):
    for i in range(len(lis)-1,-1,-1):
        if lis[i]>lis[indx]:
            return i
    return -1
def reverse(lis,index):
    left=index
    right=len(lis)-1
    while left<right:
        lis[left],lis[right]=lis[right],lis[left]
        left+=1
        right-=1
def Next_Greater_Element(num):
    if len(num)==1:
        return "-1"
    lis=list(num)
    print(lis)
    dip_indx=dipIndex(lis)
    print(dip_indx)
    if dip_indx==-1:
        return "-1"
    ceil_Indx = ceilIndex(lis, dip_indx)
    print(ceil_Indx)
    lis[ceil_Indx],lis[dip_indx]=lis[dip_indx],lis[ceil_Indx]
    reverse(lis,dip_indx+1)
    return "".join(lis)
print(Next_Greater_Element("132"))