class Solution:
    def targetIndices(self, nums, target):
        less = sum(1 for x in nums if x < target)
        equal = sum(1 for x in nums if x == target)
        return list(range(less, less + equal))

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = int(input())
    print(Solution().targetIndices(nums, target))
