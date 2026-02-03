class Solution:
    def capitalizeTitle(self, title):
        res = []
        for w in title.split():
            w = w.lower()
            if len(w) <= 2:
                res.append(w)
            else:
                res.append(w.capitalize())
        return " ".join(res)

if __name__ == "__main__":
    title = input().strip()
    print(Solution().capitalizeTitle(title))
