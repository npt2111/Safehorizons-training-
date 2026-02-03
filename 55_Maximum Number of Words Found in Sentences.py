class Solution:
    def mostWordsFound(self, sentences):
        return max(s.count(" ") + 1 for s in sentences)

if __name__ == "__main__":
    n = int(input())
    sentences = [input().strip() for _ in range(n)]
    print(Solution().mostWordsFound(sentences))
