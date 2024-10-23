class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def solve(ans, board, row):
            # If all queens are placed, increment the solution count
            if row == n:
                ans[0] += 1
                return

            for col in range(n):
                # Place the queen and mark this position on the board
                board[row][col] = True
                if is_valid(board, n, row, col):
                    # Recur to place the next queen
                    solve(ans, board, row + 1)
                # Backtrack: unmark the current cell
                board[row][col] = False

        def is_valid(board, n, row, col):
            # Check column conflicts
            for i in range(row):
                if board[i][col]:
                    return False

            # Check diagonal conflicts (upper-left diagonal)
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j]:
                    return False
                i -= 1
                j -= 1

            # Check anti-diagonal conflicts (upper-right diagonal)
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j]:
                    return False
                i -= 1
                j += 1

            # If no conflicts are found, return true
            return True

        # Initialize the answer counter and the board
        ans = [0]
        board = [[False] * n for _ in range(n)]

        # Start solving from the first row
        solve(ans, board, 0)

        # Return the number of distinct solutions
        return ans[0]


