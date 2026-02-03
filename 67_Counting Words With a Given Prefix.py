class Solution:
    def prefixCount(self, words, pref):
        c = 0
        for w in words:
            if w.startswith(pref):
                c += 1
        return c


if __name__ == "__main__":
    words = input().split()
    pref = input().strip()
    print(Solution().prefixCount(words, pref))
