def Faulty_Keyboard(name,typed):
    i =0
    j=0
    if len(name)>len(typed):
        return False
    while i <len(name) and j<len(typed):
        if name[i]==typed[j]:
            i+=1
            j+1
        elif i-1>=0 and name[i-1]==typed[j]:
            j+=1
        else:
            return False
    while j<len(typed):
        if typed[j]!=name[i-1]:
            return False
        j+=1
    return True