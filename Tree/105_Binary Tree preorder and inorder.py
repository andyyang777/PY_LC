！！！！！！！！！！！！！



超级牛逼的解释，很容易理解
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/xiong-mao-shua-ti-python3-xian-xu-zhao-gen-hua-fen/
网址在上

# Given preorder and inorder traversal of a tree, construct the binary tree. 
# 
#  Note: 
# You may assume that duplicates do not exist in the tree. 
# 
#  For example, given 
# 
#  
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7] 
# 
#  Return the following binary tree: 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7 
#  Related Topics Array Tree Depth-first Search 
#  👍 3955 👎 105


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 参考网址，无敌牛逼解法
        # https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/xiong-mao-shua-ti-python3-xian-xu-zhao-gen-hua-fen/
        
        if not preorder or not inorder: return

        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: 1 + root_idx], inorder[:root_idx])
        root.right = self.buildTree(preorder[1 + root_idx:], inorder[root_idx + 1:])

        return root

# inorder.index(preorder[0]) 这一步获取根的索引值，题目说树中的各个节点的值都不相同，也确保了这步得到的结果是唯一准确的
# 而且这个idx还能当长度用相当于 左+根 的长度，因为 左+根 和 根+左 是等长的。


# leetcode submit region end(Prohibit modification and deletion)

