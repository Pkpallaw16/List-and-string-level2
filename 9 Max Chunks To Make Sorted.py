def Max_Chunks_To_Make_Sorted(arr):
    max_chunk=0
    chunk=0
    for i in range(len(arr)):
        if arr[i]>chunk:
            chunk=arr[i]
        if chunk==i:
            max_chunk+=1

    return max_chunk

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_=0
        chunks=0
        for i in range(len(arr)):
            max_=max(max_,arr[i])
            if max_==i:
                chunks+=1
        return chunks