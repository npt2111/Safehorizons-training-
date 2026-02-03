from collections import Counter

class Solution:
    def countWords(self, words1, words2):
        c1 = Counter(words1)
        c2 = Counter(words2)
        ans = 0
        for w in c1:
            if c1[w] == 1 and c2.get(w, 0) == 1:
                ans += 1
        return ans

if __name__ == "__main__":
    words1 = input().split()
    words2 = input().split()
    print(Solution().countWords(words1, words2))
