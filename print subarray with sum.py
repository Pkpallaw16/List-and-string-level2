def print_subarray(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum1=0
            for k in range(i, j + 1):
                print(arr[k], end=" ")
                sum1+=arr[k]
            print("sum=",sum1)
            print()
print_subarray([2,3,4,5,6])