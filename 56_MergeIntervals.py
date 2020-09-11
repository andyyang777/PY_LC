# Given a collection of intervals, merge all overlapping intervals. 
# 
#  Example 1: 
# 
#  
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping. 
# 
#  NOTE: input types have been changed on April 15, 2019. Please reset to defaul
# t code definition to get new method signature. 
# 
#  
#  Constraints: 
# 
#  
#  intervals[i][0] <= intervals[i][1] 
#  
#  Related Topics Array Sort


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()

        l,r = 0,1
        while r<len(intervals):
            x1,y1 = intervals[l]
            x2,y2 = intervals[r]

            if x2>y1:
                l,r = l+1, r+1
            else:
                intervals[l] = [x1, max(y1,y2)]
                intervals.pop(r)
        return intervals


    # leetcode submit region end(Prohibit modification and deletion)
