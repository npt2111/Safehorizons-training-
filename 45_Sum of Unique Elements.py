class Solution:
    def sumOfUnique(self, nums):
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        s = 0
        for k, v in d.items():
            if v == 1:
                s += k
        return s

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().sumOfUnique(nums))
