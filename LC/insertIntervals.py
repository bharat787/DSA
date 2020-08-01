class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        if(len(intervals) == 0):
            return []
        
        if(len(intervals) == 1):
            return intervals
        
        intervals = sorted(intervals)
        print(intervals)
        ret = [intervals[0]]
        
        i = 0
        j = 1
        while (j < len(intervals)):
            if(ret[i][1] >= intervals[j][0]):
                ret[i][0] = min(ret[i][0], intervals[j][0])
                ret[i][1] = max(ret[i][1], intervals[j][1])
                j += 1
            else:
                ret.append(intervals[j])
                i += 1
                j += 1
                
        return ret