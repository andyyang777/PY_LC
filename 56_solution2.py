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
        if intervals == []:
            return []
        res = []

        intervals.sort()
        for interval in intervals:
            if res == [] or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

    # leetcode submit region end(Prohibit modification and deletion)
