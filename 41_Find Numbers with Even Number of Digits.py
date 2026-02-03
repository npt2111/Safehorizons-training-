class Solution:
    def findNumbers(self, nums):
        c = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                c += 1
        return c

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().findNumbers(nums))
