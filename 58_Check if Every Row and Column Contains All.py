class Solution:
    def checkValid(self, matrix):
        n = len(matrix)
        target = set(range(1, n + 1))
        
        for i in range(n):
            if set(matrix[i]) != target:
                return False
            col = {matrix[r][i] for r in range(n)}
            if col != target:
                return False
        
        return True

if __name__ == "__main__":
    import ast
    matrix = ast.literal_eval(input().strip())
    print(Solution().checkValid(matrix))
