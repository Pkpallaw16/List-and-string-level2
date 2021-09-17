def Container_With_Most_Water(height):
    maxwater=0
    i=0
    j=len(height)-1
    while i<j:
        l=j-i
        h=min(height[i],height[j])
        water=l*h
        maxwater=max(maxwater,water)
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return maxwater       