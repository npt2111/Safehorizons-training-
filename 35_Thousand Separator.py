class Solution:
    def thousandSeparator(self, n):
        s = str(n)
        res = ""
        cnt = 0
        
        for c in reversed(s):
            if cnt == 3:
                res = "." + res
                cnt = 0
            res = c + res
            cnt += 1
        
        return res

if __name__ == "__main__":
    n = int(input())
    print(Solution().thousandSeparator(n))
