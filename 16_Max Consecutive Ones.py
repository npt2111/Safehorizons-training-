class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        curr = 0

        for n in nums:
            if n == 1:
                curr += 1
                if curr > max_count:
                    max_count = curr
            else:
                curr = 0

        return max_count


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
    print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))
