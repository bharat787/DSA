def longestPalindrome(s):
    maxstr = ''
    k = 0
    for l in s:
        print(l)
        freq = s.count(l)
        print('freq ', freq)
        if(freq > 1):
            try:
                print(s[k+1:])
                ind = k+1 + s[k+1:].index(l)
            except:
                ind = k
            print('index', ind)
        while(freq >= 2):
            curstr = s[k: ind+1]
            rev = curstr[::-1]
            print("current string", curstr)
            print("rev string", rev)
            if(curstr == rev):
                tempstr = curstr
                print('current longest', tempstr)
                if(len(tempstr) > len(maxstr)): 
                    maxstr = tempstr
            try:
                ind = k + s[ind+1:].index(l)
            except:
                ind = k
            freq -= 1
        k += 1

    print("max", maxstr)

longestPalindrome('babad')
            
            