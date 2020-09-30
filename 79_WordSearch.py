# Given a 2D board and a word, find if the word exists in the grid. 
# 
#  The word can be constructed from letters of sequentially adjacent cell, where
#  "adjacent" cells are those horizontally or vertically neighboring. The same let
# ter cell may not be used more than once. 
# 
#  Example: 
# 
#  
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#  
# 
#  
#  Constraints: 
# 
#  
#  board and word consists only of lowercase and uppercase English letters. 
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  1 <= word.length <= 10^3 
#  
#  Related Topics Array Backtracking 
#  👍 4431 👎 204


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        def dfs(index,x,y):
            if index == len(word) - 1:
                return True
            temp = board[x][y]
            board[x][y] = 0
            for i, j in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 0<=i<n and 0<=j<m and board[i][j] != 0 and board[i][j] == word[index+1]:
                    if dfs(index+1, i, j):
                        return True
            board[x][y] = temp
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(0,i,j):
                        return True
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
