# Given a non-empty binary search tree and a target value, find the value in the
#  BST that is closest to the target. 
# 
#  Note: 
# 
#  
#  Given target value is a floating point. 
#  You are guaranteed to have only one unique value in the BST that is closest t
# o the target. 
#  
# 
#  Example: 
# 
#  
# Input: root = [4,2,5,1,3], target = 3.714286
# 
#     4
#    / \
#   2   5
#  / \
# 1   3
# 
# Output: 4
#  
#  Related Topics Binary Search Tree 
#  👍 841 👎 65


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    Time: O(H), because one goes from root down to a leaf.
    space: O(1)
    
    
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(closest, root.val, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest

# leetcode submit region end(Prohibit modification and deletion)
