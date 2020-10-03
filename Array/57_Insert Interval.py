# Given a set of non-overlapping intervals, insert a new interval into the inter
# vals (merge if necessary). 
# 
#  You may assume that the intervals were initially sorted according to their st
# art times. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10]. 
# 
# 
#  Example 3: 
# 
#  
# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]
#  
# 
#  Example 4: 
# 
#  
# Input: intervals = [[1,5]], newInterval = [2,3]
# Output: [[1,5]]
#  
# 
#  Example 5: 
# 
#  
# Input: intervals = [[1,5]], newInterval = [2,7]
# Output: [[1,7]]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= intervals.length <= 104 
#  intervals[i].length == 2 
#  0 <= intervals[i][0] <= intervals[i][1] <= 105 
#  intervals is sorted by intervals[i][0] in ascending order. 
#  newInterval.length == 2 
#  0 <= newInterval[0] <= newInterval[1] <= 105 
#  
#  Related Topics Array Sort 
#  👍 2143 👎 215


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    
    
    #这题用到的是贪心算法
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newInt_start, newInt_end = newInterval
        res = []
        idx, n = 0, len(intervals)

        while idx<n and intervals[idx][0]<newInt_start:
            res.append(intervals[idx])
            idx += 1

        if not res or res[-1][1] < newInt_start:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], newInt_end)

        while idx<n:
            res_interval = intervals[idx]
            new_star, new_end = res_interval
            idx += 1

            if res[-1][1]<new_star:
                res.append(res_interval)
            else:
                res[-1][1] = max(res[-1][1], new_end)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
