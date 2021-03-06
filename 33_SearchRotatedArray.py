# You are given an integer array nums sorted in ascending order, and an integer 
# target. 
# 
#  Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [
# 0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]). 
# 
#  If target is found in the array return its index, otherwise, return -1. 
# 
#  
#  Example 1: 
#  Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#  Example 2: 
#  Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#  Example 3: 
#  Input: nums = [1], target = 0
# Output: -1
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5000 
#  -10^4 <= nums[i] <= 10^4 
#  All values of nums are unique. 
#  nums is guranteed to be rotated at some pivot. 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics Array Binary Search 
#  👍 5862 👎 511


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1

        l, r = 0, len(nums) - 1
        while l <= r:  #### !!!!!!!!!!!特别注意这里，要等于才可以，因为有l = r = mid的情况发生
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if nums[mid] >= nums[l]:  # 说明mid的左半部分是有序的,而且要注意，这里mid要取到等号，因为下面的if判断里mid没有用到，所以这里一定要有等号
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # 说明mid比开头第一个数小，就说明mid的右边是有序的
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

# leetcode submit region end(Prohibit modification and deletion)
