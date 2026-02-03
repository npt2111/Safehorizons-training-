class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = j = 0
        content = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1

        return content


if __name__ == "__main__":
    sol = Solution()
    print(sol.findContentChildren([1,2,3], [1,1]))      # 1
    print(sol.findContentChildren([1,2], [1,2,3]))      # 2
