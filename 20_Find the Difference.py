class Solution:
    def findTheDifference(self, s, t):
        x = 0
        for c in s:
            x ^= ord(c)
        for c in t:
            x ^= ord(c)
        return chr(x)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))
    print(sol.findTheDifference("", "y"))
