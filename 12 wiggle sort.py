def wiggle_sort(arr):
    for i in range(len(arr)):
        if i%2==0:
            if arr[i]>arr[i+1]:
                arr[i],arr[i + 1]=arr[i+1],arr[i]
            else:
                if arr[i]<arr[i+1]:
                    arr[i],arr[i + 1]=arr[i+1],arr[i]

    print(arr)