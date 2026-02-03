class Solution:
    def largestAltitude(self, gain):
        cur = 0
        mx = 0
        for g in gain:
            cur += g
            if cur > mx:
                mx = cur
        return mx

if __name__ == "__main__":
    gain = list(map(int, input().split()))
    print(Solution().largestAltitude(gain))
