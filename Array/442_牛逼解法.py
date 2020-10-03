# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements ap
# pear twice and others appear once. 
# 
#  Find all the elements that appear twice in this array. 
# 
#  Could you do it without extra space and in O(n) runtime? 
#  
#  Example: 
#  
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [2,3]
#  Related Topics Array 
#  👍 2824 👎 163


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 这题，题目暗示了一个trick，因为1 ≤ a[i] ≤ n (n = size of array)，所以的话把nums这个列表里的内容转换为
        # 内容的索引。比如[4,3,2,7,8,2,3,1]，可以知道这个list，长度为8，那么索引就是0-7，符合要求。
        # 那么如果这个数字出现过两次，就表示这个数字本身-1后的那个地方的索引对应的数字会被操作，利用这一点
        # 最后就看那个位置的值，如果那个地方的值是负的，那么就说明这个地方已经被搞了一次，那么现在再来搞，就说明他出现了两次，所以这个
        # 索引n就出现了两次，要返回的是这个被当成索引来用的数字自己本身，因为可能已经被搞了，所以你就把他搞成绝对值来append就行
        res = []
        for n in nums:
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] *= -1
            else:
                res.append(abs(n))
        return res

# leetcode submit region end(Prohibit modification and deletion)
