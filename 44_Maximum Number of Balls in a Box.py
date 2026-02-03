class Solution:
    def countBalls(self, lowLimit, highLimit):
        cnt = {}
        mx = 0
        for x in range(lowLimit, highLimit + 1):
            s = sum(int(d) for d in str(x))
            cnt[s] = cnt.get(s, 0) + 1
            if cnt[s] > mx:
                mx = cnt[s]
        return mx

if __name__ == "__main__":
    lowLimit = int(input().strip())
    highLimit = int(input().strip())
    print(Solution().countBalls(lowLimit, highLimit))
