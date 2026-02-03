class Solution:
    def destCity(self, paths):
        out = set()
        for a, b in paths:
            out.add(a)
        for a, b in paths:
            if b not in out:
                return b

if __name__ == "__main__":
    n = int(input())
    paths = [input().split(",") for _ in range(n)]
    paths = [[p[0].strip(), p[1].strip()] for p in paths]
    print(Solution().destCity(paths))
