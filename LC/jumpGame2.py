def jump(nums):
    
        count = 0
        last = len(nums)-1
        index = 0
        
        while index < last:
            best_jump_index =index + nums[index]

            min_r , max_r = index + 1 , best_jump_index
            if max_r >= last:
                count+=1
                break
                
            best_jump_len = best_jump_index + nums[best_jump_index]
            
            for i in range(min_r,max_r):
                current_jump = nums[i]
                if best_jump_len < i + current_jump:
                    best_jump_index = i
                    best_jump_len = i + current_jump
    
            index =  best_jump_index
            count+=1
            
        return count
        
jump([3, 2, 2, 5, 7, 2, 3, 6, 7, 3, 1])