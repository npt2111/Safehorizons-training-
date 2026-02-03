class Solution:
    def checkString(self, s):
        return "ba" not in s

if __name__ == "__main__":
    s = input().strip()
    print(str(Solution().checkString(s)).lower())
