class Solution:
    def areOccurrencesEqual(self, s):
        from collections import Counter
        c = Counter(s)
        return len(set(c.values())) == 1

if __name__ == "__main__":
    s = input().strip()
    print(str(Solution().areOccurrencesEqual(s)).lower())
