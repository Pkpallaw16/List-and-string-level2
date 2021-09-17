def Boats_to_Save_People(arr,limit):
    arr.sort()
    l=0
    r=len(arr)-1
    count=0
    while l<=r:
        if arr[l]+arr[r]<limit:
            l+=1
            r-=1
            count+=1

        else:
            r -= 1
            count += 1
    return count
