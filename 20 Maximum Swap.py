def Maximum_Swap(num):
    num=str(num)
    last_occ=[0 for i in range(10)]
    for i in range(len(num)):
        last_occ[num[i]]=i
    for i in range(len(num)):
        digit=num[i]-'0'
        indx=i
        for j in range(9,digit,-1):
            if last_occ[j]>i:
                indx=last_occ[j]
                break
        if indx!=i:
            strlst = list(num)
            strlst[i], strlst[indx] = strlst[indx], strlst[i]
            num="".join(strlst)
    return int(num)