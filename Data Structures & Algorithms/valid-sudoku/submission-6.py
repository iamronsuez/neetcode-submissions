class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        _boxes = defaultdict(set)
        _rows = defaultdict(set)
        _columns = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                _value = board[i][j]
                if _value == ".":
                    continue
                if _value in _rows[i]:
                    return False
                _rows[i].add(_value)
                if _value in _columns[j]:
                    return False
                _columns[j].add(_value)
                if _value in _boxes[(i // 3, j // 3)]:
                    return False
                _boxes[(i // 3, j // 3)].add(_value)
        return True


