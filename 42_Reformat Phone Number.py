class Solution:
    def reformatNumber(self, number):
        s = ''.join(c for c in number if c.isdigit())
        res = []
        i = 0
        n = len(s)
        while n - i > 4:
            res.append(s[i:i+3])
            i += 3
        r = n - i
        if r == 4:
            res.append(s[i:i+2])
            res.append(s[i+2:i+4])
        else:
            res.append(s[i:])
        return "-".join(res)

if __name__ == "__main__":
    number = input().strip()
    print(Solution().reformatNumber(number))
