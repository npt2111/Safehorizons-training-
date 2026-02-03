class Solution:
    def minimumCost(self, cost):

        cost.sort(reverse=True)
        total = 0
        
        for i, c in enumerate(cost):

            if i % 3 != 2:
                total += c
        
        return total

if __name__ == "__main__":
    import ast
    cost = ast.literal_eval(input().strip())
    print(Solution().minimumCost(cost))
