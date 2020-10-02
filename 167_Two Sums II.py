# Given an array of integers that is already sorted in ascending order, find two
#  numbers such that they add up to a specific target number. 
# 
#  The function twoSum should return indices of the two numbers such that they a
# dd up to the target, where index1 must be less than index2. 
# 
#  Note: 
# 
#  
#  Your returned answers (both index1 and index2) are not zero-based. 
#  You may assume that each input would have exactly one solution and you may no
# t use the same element twice. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#  
# 
#  Example 2: 
# 
#  
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
#  
# 
#  Example 3: 
# 
#  
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 3 * 104 
#  -1000 <= nums[i] <= 1000 
#  nums is sorted in increasing order. 
#  -1000 <= target <= 1000 
#  
#  Related Topics Array Two Pointers Binary Search 
#  👍 1921 👎 648


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low+1, high+1]
            elif total < target:
                low += 1
            else:
                high -= 1
        return [0,0]
        
# leetcode submit region end(Prohibit modification and deletion)
