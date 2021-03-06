# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elemen
# ts appear twice and others appear once. 
# 
#  Find all the elements of [1, n] inclusive that do not appear in this array. 
# 
#  Could you do it without extra space and in O(n) runtime? You may assume the r
# eturned list does not count as extra space. 
# 
#  Example:
#  
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]
#  
#  Related Topics Array 
#  👍 3172 👎 260


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums) + 1
        res = []
        nums = set(nums)

        for x in range(1, l):
            if x not in nums:
                res.append(x)
        return res

# leetcode submit region end(Prohibit modification and deletion)
