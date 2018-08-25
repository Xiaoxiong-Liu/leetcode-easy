"""
有效的数独
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/30/

"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] not in s:
                    if board[i][j] != ".":
                        s.add(board[i][j])
                else:
                    return False

        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] not in s:
                    if board[j][i] != ".":
                        s.add(board[j][i])
                else:
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for m in range(3):
                    for n in range(3):
                        if board[i + m][j + n] not in s:
                            if board[i + m][j + n] != ".":
                                s.add(board[i + m][j + n])
                        else:
                            return False
        return True
