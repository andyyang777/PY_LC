# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions su
# rrounded by 'X'. 
# 
#  A region is captured by flipping all 'O's into 'X's in that surrounded region
# . 
# 
#  Example: 
# 
#  
# X X X X
# X O O X
# X X O X
# X O X X
#  
# 
#  After running your function, the board should be: 
# 
#  
# X X X X
# X X X X
# X X X X
# X O X X
#  
# 
#  Explanation: 
# 
#  Surrounded regions shouldn’t be on the border, which means that any 'O' on th
# e border of the board are not flipped to 'X'. Any 'O' that is not on the border 
# and it is not connected to an 'O' on the border will be flipped to 'X'. Two cell
# s are connected if they are adjacent cells connected horizontally or vertically.
#  
#  Related Topics Depth-first Search Breadth-first Search Union Find 
#  👍 2090 👎 708


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return ## 边界条件判断
        row = len(board)
        column = len(board[0])

        def dfs(x,y):
            board[x][y] = "B"
            for nx, ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if 1<=nx<row and 1<=ny<column and board[nx][ny] == "O":
                    dfs(nx,ny)

        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i,0)
            # 最后一列
            if board[i][column-1] == "O":
                dfs(i,column-1)

        for j in range(column):
            if board[0][j] == "O":
                dfs(0,j)
            if board[row-1][j] == "O":
                dfs(row-1,j)

        for i in range(row):
            for j in range(column):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"

# leetcode submit region end(Prohibit modification and deletion)
