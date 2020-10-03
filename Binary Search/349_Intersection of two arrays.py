# Given two arrays, write a function to compute their intersection. 
# 
#  Example 1: 
# 
#  
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4] 
#  
# 
#  Note: 
# 
#  
#  Each element in the result must be unique. 
#  The result can be in any order. 
#  
# 
#  
#  Related Topics Hash Table Two Pointers Binary Search Sort 
#  👍 998 👎 1308


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # method 1: built-in function
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1&set2)

      
        
# leetcode submit region end(Prohibit modification and deletion)
