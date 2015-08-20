import copy

class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        board = ['.' * n] * n
        col_empty = [True] * n
        up_diag_empty = [True] * (2*n - 1)
        down_diag_empty = [True] * (2*n - 1)
        solutions = []
        
        def is_safe(r, c):
            return col_empty[c] and up_diag_empty[r+c] and down_diag_empty[n-1+r-c]
        
        def place_queen(r, c):
            board[r] = board[r][:c] + "Q" + board[r][c+1:]
            col_empty[c] = False
            up_diag_empty[r+c] = False
            down_diag_empty[n-1+r-c] = False
        
        def remove_queen(r, c):
            board[r] = board[r][:c] + "." + board[r][c+1:]
            col_empty[c] = True
            up_diag_empty[r+c] = True
            down_diag_empty[n-1+r-c] = True
        
        def find_solution(r):
            if r == n:
                solutions.append(copy.deepcopy(board))
                return
            
            for c in range(n):
                if is_safe(r, c):
                    place_queen(r, c)
                    find_solution(r+1)
                    remove_queen(r, c)

        find_solution(0)
        return solutions

        
if __name__ == "__main__":
    solu = Solution()
    ret = solu.solveNQueens(4)
    for r in ret:
        print(r)
