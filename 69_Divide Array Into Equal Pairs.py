class Solution:
    def divideArray(self, nums):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        return all(v % 2 == 0 for v in freq.values())


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().divideArray(nums))

