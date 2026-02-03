class Solution:
    def countElements(self, nums):
        mn, mx = min(nums), max(nums)
        return sum(mn < x < mx for x in nums)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().countElements(nums))
