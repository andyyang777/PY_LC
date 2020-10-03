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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []

        while idx<n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1],new_end)


        while idx<n:
            interval = intervals[idx]
            start, end = interval
            idx += 1

            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
        return output
        
# leetcode submit region end(Prohibit modification and deletion)
