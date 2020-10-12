# Given an array of integers nums, write a method that returns the "pivot" index
#  of this array. 
# 
#  We define the pivot index as the index where the sum of all the numbers to th
# e left of the index is equal to the sum of all the numbers to the right of the i
# ndex. 
# 
#  If no such index exists, we should return -1. If there are multiple pivot ind
# exes, you should return the left-most pivot index. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the su
# m of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
#  
# 
#  
#  Constraints: 
# 
#  
#  The length of nums will be in the range [0, 10000]. 
#  Each element nums[i] will be an integer in the range [-1000, 1000]. 
#  
#  Related Topics Array 
#  👍 1308 👎 266


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # 前缀和
        s = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (s - leftsum - x):
                return i
            leftsum += x
        return -1

        # Time: O(N), N is the length of nums
        # Space: O(1), only use s and leftsum to store the results.

# leetcode submit region end(Prohibit modification and deletion)
