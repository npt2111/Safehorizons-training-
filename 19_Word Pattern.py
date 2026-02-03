class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False

        p2w = {}
        w2p = {}

        for p, w in zip(pattern, words):
            if p in p2w and p2w[p] != w:
                return False
            if w in w2p and w2p[w] != p:
                return False
            p2w[p] = w
            w2p[w] = p

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))
    print(sol.wordPattern("abba", "dog cat cat fish"))
    print(sol.wordPattern("aaaa", "dog cat cat dog"))
