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
    directions = [(0,-1), (-1,0),(0,1),(1,0)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) ## 行数
        n = len(board[0]) ##列数

        marked = [[False for _ in range(n)] for _ in range(m)] ## 一开始都设为假，说明都没有访问过

        for i in range(m): #对每个格子都从头开始搜索
            for j in range(n):
                if self.search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def search_word(self,board, word, index, x, y, marked, m, n):
        if index == len(word) - 1:
            return board[x][y] == word[index]
        # 如果当index已经搞到word的最后一个了，就说明前面都还没出错
        # 所以此时如果board里这时候的x，y还和word里最后一个匹配，就说明全都匹配

        # 中间的匹配里，再继续搜索
        if board[x][y] == word[index]:
            # 先暂存这个位置，如果不成功的话则释放掉这个位置
            marked[x][y] = True
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]

                if 0 <= new_x < m and 0 <= new_y < n \
                        and not marked[new_x][new_y] \
                        and self.search_word(board,word,index+1, new_x, new_y, marked, m,n):
                    return True

            marked[x][y] = False
        return False


#         (x-1,y)
# (x,y-1) (x,y) (x,y+1)
#         (x+1,y)



# leetcode submit region end(Prohibit modification and deletion)
