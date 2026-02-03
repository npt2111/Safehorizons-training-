class Solution:
    def smallestEqual(self, nums):
        for i, v in enumerate(nums):
            if i % 10 == v:
                return i
        return -1

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().smallestEqual(nums))
