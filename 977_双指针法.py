# Given an array of integers A sorted in non-decreasing order, return an array o
# f the squares of each number, also in sorted non-decreasing order. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 10000 
#  -10000 <= A[i] <= 10000 
#  A is sorted in non-decreasing order. 
#  
#  
#  Related Topics Array Two Pointers 
#  👍 1477 👎 98


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # 思路，双指针
        # 因为就是数组已经是sort了的，排序好的，所以负数部分的话平方后是降序，而正数部分平方后就是升序
        # 所以只需要搞两个指针，一个正走，一个反走即可
        # 然后要考虑就是负数的走完了，正数没走完，还有正数走完了负数没走完，这两种情况
        N = len(A)
        positive = 0
        while positive < N and A[positive] < 0:
            positive += 1
        negative = positive - 1  # 负指针的初始位置就是positive的左边一个
        res = []

        while 0 <= negative and positive < N:
            if A[negative] ** 2 < A[positive] ** 2:
                res.append(A[negative] ** 2)
                negative -= 1
            else:
                res.append(A[positive] **2)
                positive += 1
        while negative >= 0:
            res.append(A[negative] ** 2)
            negative -= 1
        while positive < N:
            res.append(A[positive] ** 2)
            positive += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
