class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        res = []

        for i, w in enumerate(words, start=1):
            if w[0] in vowels:
                goat = w + "ma"
            else:
                goat = w[1:] + w[0] + "ma"
            
            goat += "a" * i
            res.append(goat)

        return " ".join(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.toGoatLatin("I speak Goat Latin"))
    print(sol.toGoatLatin("The quick brown fox jumped over the lazy dog"))
