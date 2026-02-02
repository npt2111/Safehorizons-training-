class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0

        for i, x in enumerate(nums):
            if left == total - left - x:
                return i
            left += x

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.pivotIndex([1,7,3,6,5,6]))
    print(sol.pivotIndex([1,2,3]))
    print(sol.pivotIndex([2,1,-1]))
