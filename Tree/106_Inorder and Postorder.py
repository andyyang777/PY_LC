# Given inorder and postorder traversal of a tree, construct the binary tree. 
# 
#  Note: 
# You may assume that duplicates do not exist in the tree. 
# 
#  For example, given 
# 
#  
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3] 
# 
#  Return the following binary tree: 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  Related Topics Array Tree Depth-first Search 
#  👍 2109 👎 38


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return

        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:idx], postorder[0:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])

        return root
        
# leetcode submit region end(Prohibit modification and deletion)
