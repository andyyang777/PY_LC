# Given an array nums containing n distinct numbers taken from 0, 1, 2, ..., n, 
# return the one that is missing from the array. 
# 
#  Follow up: Could you implement a solution using only constant extra space com
# plexity and linear runtime complexity? 
# 
#  
#  Example 1: 
#  Input: nums = [3,0,1]
# Output: 2
#  Example 2: 
#  Input: nums = [0,1]
# Output: 2
#  Example 3: 
#  Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
#  Example 4: 
#  Input: nums = [0]
# Output: 1
#  
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 104 
#  0 <= nums[i] <= n 
#  All the numbers of nums are unique. 
#  
#  Related Topics Array Math Bit Manipulation 
#  👍 2110 👎 2327


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # 方法一，排序
        # 时间复杂度：O(nlogn)。由于排序的时间复杂度为 O(logn)，
        # 扫描数组的时间复杂度为 O(n)，因此总的时间复杂度为 O(nlogn)。

        # 空间复杂度：O(1)O(1) 或 O(n)O(n)。空间复杂度取决于使用的排序算法，
        # 根据排序算法是否进行原地排序（即不使用额外的数组进行临时存储），空间复杂度为 O(1)O(1) 或 O(n)O(n)。

        # nums.sort()
        # if nums[-1] != len(nums):
        #     return len(nums)
        # elif nums[0] != 0:
        #     return 0
        #
        # for i in range(1, len(nums)):
        #     exp_num = nums[i - 1] + 1
        #     if nums[i] != exp_num:
        #         return exp_num
        ######################################################################

        # 方法二，哈希表
        # 时间复杂是On，对set的插入都是O1，插了n个，所以是On，集合查询每个O1，查n+1次，也是On，所以最后是On
        # 空间复杂度 On，集合中存储n个数
        # nums_set = set(nums)
        # n = len(nums)+1
        # for number in range(n):
        #     if number not in nums_set:
        #         return number
        ######################################################################


        # 方法三，求和公式
        # 时间复杂度：O(n)。求出数组中所有数的和的时间复杂度为 O(n)，高斯求和公式的时间复杂度为 O(1)，因此总的时间复杂度为 O(n)。
        # 空间复杂度：O(1)。算法中只用到了 O(1) 的额外空间，用来存储答案。
        # 

        exp_sum = len(nums) * (len(nums)+1) // 2
        actual_sum = sum(nums)
        return exp_sum-actual_sum


# leetcode submit region end(Prohibit modification and deletion)
