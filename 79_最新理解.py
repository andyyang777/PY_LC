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
    #         (x-1,y)
    # (x,y-1) (x,y) (x,y+1)
    #         (x+1,y)
    # directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(index, x, y):
            if index == len(word) - 1:
                return True

            temp = board[x][y]
            board[x][y] = 1
            for nx, ny in [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]:
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != 1 and board[nx][ny] == word[index + 1]:
                    if dfs(index+1, nx, ny):
                        return True
            board[x][y] = temp

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(0,i,j):
                        return True
        return False
#         (x-1,y)
# (x,y-1) (x,y) (x,y+1)
#         (x+1,y)


# leetcode submit region end(Prohibit modification and deletion)
