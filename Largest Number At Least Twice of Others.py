import sys
def dominantIndex(nums):
    max1=-sys.maxsize
    max2=-sys.maxsize
    for val in nums:
        if val>max1:
            max2=max1
            max1=val
        elif val>max2:
            max2=val

    return max1 if max1>2*max2 else -1