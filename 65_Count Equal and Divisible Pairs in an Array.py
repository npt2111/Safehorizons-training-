class Solution:
    def countPairs(self, nums, k):
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    cnt += 1
        return cnt


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    print(Solution().countPairs(nums, k))
