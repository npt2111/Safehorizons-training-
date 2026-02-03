class Solution:
    def countEven(self, num):
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
        cnt = 0
        for i in range(1, num + 1):
            if digit_sum(i) % 2 == 0:
                cnt += 1
        return cnt


if __name__ == "__main__":
    num = int(input())
    print(Solution().countEven(num))
