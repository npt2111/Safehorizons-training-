class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    print(sol.topKFrequent([1], 1))
    print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))
