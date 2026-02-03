class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = {}

        for a in nums1:
            for b in nums2:
                s = a + b
                count[s] = count.get(s, 0) + 1

        res = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                res += count.get(target, 0)

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))
    print(sol.fourSumCount([0], [0], [0], [0]))
