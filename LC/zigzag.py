def zigzag(s, num):
    res = ''
    l = list(s)
    k = 0
    while(l != []):
        res += l[k]
        del(l[k])
        k += num
        if(k > len(l)):
            k = 0
        
    print(res)
    
zigzag('PAYPALISHIRING', 3)