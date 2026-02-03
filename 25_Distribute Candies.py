class Solution:
    def distributeCandies(self, candyType):
        kinds = len(set(candyType))
        limit = len(candyType) // 2
        return min(kinds, limit)


if __name__ == "__main__":
    sol = Solution()
    print(sol.distributeCandies([1,1,2,2,3,3]))  # 3
    print(sol.distributeCandies([1,1,2,3]))      # 2
    print(sol.distributeCandies([6,6,6,6]))      # 1
