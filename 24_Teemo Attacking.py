class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries or duration == 0:
            return 0

        total = 0

        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i+1] - timeSeries[i]
            total += min(duration, gap)

        # add duration for the last attack
        total += duration
        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPoisonedDuration([1,4], 2))  # 4
    print(sol.findPoisonedDuration([1,2], 2))  # 3
