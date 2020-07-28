def remDup(l):
    
    for i in range(len(l) - 1):
        print(i, "  ", i+1)
        try:
            while(l[i] == l[i+1]):
                del l[i+1]
        except:
            print(l)
remDup([1,2,2,3,3,3,4,4,5,6,6,6,7])