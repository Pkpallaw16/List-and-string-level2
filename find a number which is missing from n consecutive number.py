
def find_missing_value(lis,lo,hi):
    if lo==hi:
        return lo
    mid=int((lo+hi)/2)
    if lis[0]+mid==lis[mid]:
        return find_missing_value(lis,mid+1,hi)
    else:
        return find_missing_value(lis,lo,mid-1)

def find_missing_val_helper(lis):
    indx=find_missing_value(lis,0,len(lis)-1)
    if len(lis)==0 or len(lis)==1:
        print("No value is missing")
        return
    if indx==len(lis)-1 and lis[indx-1]+1==lis[indx]:
        print("No value is missing")
    elif lis[0]+indx==lis[indx]:
        print(lis[indx]+1)
    else:
        print(lis[indx]-1)

l=[2,3,4,5,6,7,8,9,10,12,13,14]
find_missing_val_helper(l)
"""
[5]
[5, 6]
[4, 6]
[3,4,5,6,8,9]
[3,4,5,6,7,9]
[3,4,5,6,7,8,9]
[3,5,6,7,8]
[2,3,4,5,6,7,8,9,10,12,13,14]"""