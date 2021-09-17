import sys
def Max_Chunks_To_Make_Sorted(arr):
    n=len(arr)
    right_min=[0 for i in range(n+1)]
    right_min[n]=sys.maxsize
    chunks=0
    for i in range(n-1,-1,-1):
        right_min[i]=min(right_min[i+1],arr[i])
    left_max=-sys.maxsize
    for i in range(len(arr)):
        left_max=max(left_max,arr[i])
        if left_max<= right_min[i+1]:
            chunks+=1
    return chunks