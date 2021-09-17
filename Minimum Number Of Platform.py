
def Minimum_Number_Of_Platform(arr,dep):
    arr.sort()
    dep.sort()
    n=len(arr)
    i=0
    j=0
    cmax=0
    omax=0
    while i<n:
        if arr[i]<=dep[j]:
            cmax+=1
            i+=1
        else:
            cmax-=1
            j+=1
        omax=max(omax,cmax)
    return omax



