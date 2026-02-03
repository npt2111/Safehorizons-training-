class Solution:
    def sumZero(self, n: int):
        res = []
        
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        
        if n % 2 == 1:
            res.append(0)
        
        return res


if __name__ == "__main__":
    n = int(input("Enter n: "))
    sol = Solution()
    result = sol.sumZero(n)
    print(result)
    print("Sum check:", sum(result))
