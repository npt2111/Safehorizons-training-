class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(1 for c in stones if c in jewel_set)

if __name__ == "__main__":
    sol = Solution()
    print(sol.numJewelsInStones("aA", "aAAbbbb"))  # 3
    print(sol.numJewelsInStones("z", "ZZ"))        # 0
