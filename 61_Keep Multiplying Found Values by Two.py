class Solution:
    def findFinalValue(self, nums, original):
        s = set(nums)
        while original in s:
            original *= 2
        return original

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    original = int(input())
    print(Solution().findFinalValue(nums, original))
