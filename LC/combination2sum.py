def backtracking(ans, temp, index, nums, target):
    #print('called')
    if( target == 0):
        if temp not in ans:
            ans.append(temp)
            #print('called1')
            
            #print(ans)
            
        return 0
    
    elif ( target < 0):
        #print('called2')
        return 0
    
    else:
        #print('called3')
        for i in range(index, len(nums)):
            #print(i)
            temp.append(nums[i])
            print(temp, " ")
            #print(temp)
            backtracking(ans, temp, i + 1, nums, target - nums[i])
            print(temp, " ")
            del temp[-1]
            print(temp, "\n")
            
        return 1
    
candidates  = [1, 1, 2, 5, 6, 7, 10]
target = 8
temp  = []
ans = []
backtracking(ans, temp, 0, candidates, target)
print(ans)