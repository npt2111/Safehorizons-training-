class Solution:
    def secondHighest(self, s):
        st = set()
        for c in s:
            if c.isdigit():
                st.add(int(c))
        if len(st) < 2:
            return -1
        a = sorted(st, reverse=True)
        return a[1]

if __name__ == "__main__":
    s = input().strip()
    print(Solution().secondHighest(s))
