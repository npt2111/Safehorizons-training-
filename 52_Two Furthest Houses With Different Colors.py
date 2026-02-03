class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        ans = 0
        for i in range(n):
            for j in range(n - 1, i, -1):
                if colors[i] != colors[j]:
                    ans = max(ans, j - i)
                    break
        return ans

if __name__ == "__main__":
    colors = list(map(int, input().split()))
    print(Solution().maxDistance(colors))
