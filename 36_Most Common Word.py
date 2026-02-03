class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(w.lower() for w in banned)
        cleaned = ""
        for c in paragraph:
            if c.isalpha():
                cleaned += c.lower()
            else:
                cleaned += " "
        counts = {}
        for w in cleaned.split():
            if w not in banned_set:
                counts[w] = counts.get(w, 0) + 1
        return max(counts, key=counts.get)

if __name__ == "__main__":
    paragraph = input().strip()
    banned = input().strip().split()
    print(Solution().mostCommonWord(paragraph, banned))
