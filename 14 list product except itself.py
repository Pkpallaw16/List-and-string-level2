def array_product_eccept_itself(arr):
    right_product=[0 for i in range(len(arr))]
    mult=1
    for i in range(len(arr)-1,-1,-1):
        mult=mult*arr[i]
        right_product[i]=mult
    pro_ex=[0 for i in range(len(arr))]
    prod=1
    for i in range(len(arr)-1):
        lp=prod
        rp=right_product[i+1]
        pro_ex[i]=lp*rp
        prod*=arr[i]
    pro_ex[len(arr)-1]=prod
    print(pro_ex)

arr=[1,2,3,4]
array_product_eccept_itself(arr)


