def Range_Addition(length,updates):
    lis=[0 for i in range(length)]
    for i in range(len(updates)):
        st=updates[i][0]
        end=updates[i][1]
        inc=updates[i][3]
        lis[st]+=inc
        if end!=length-1:
            lis[end+1]-=inc
    sum=0
    for i in range(length):
        sum+=lis[i]
        lis[i]=sum
    return lis
