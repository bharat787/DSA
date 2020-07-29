def permutation(lst):
    
    if(len(lst) == 0):
        return []
    if(len(lst) == 1):
        return [lst]
    
    l = []
    
    for i in range (len(lst)):
        m = lst[i]
        
        remLst = lst[:i] + lst[i+1:]
        
        for p in permutation(remLst):
            if ([m] + p) not in l:
                l.append([m] + p)
            
    return l

k = permutation([2,2,7,5,4,3,2,2,1])
print(sorted(k))