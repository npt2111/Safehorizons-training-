class Solution:
    def mostFrequent(self, nums, key):
        freq = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                t = nums[i + 1]
                freq[t] = freq.get(t, 0) + 1
        return max(freq, key=freq.get)


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    key = int(input().strip())
    print(Solution().mostFrequent(nums, key))
