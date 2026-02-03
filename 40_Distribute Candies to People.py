class Solution:
    def distributeCandies(self, candies, num_people):
        res = [0] * num_people
        give = 1
        i = 0
        while candies > 0:
            idx = i % num_people
            g = min(give, candies)
            res[idx] += g
            candies -= g
            give += 1
            i += 1
        return res

if __name__ == "__main__":
    candies = int(input().strip())
    num_people = int(input().strip())
    print(Solution().distributeCandies(candies, num_people))
