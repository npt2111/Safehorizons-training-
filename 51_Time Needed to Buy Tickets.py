class Solution:
    def timeRequiredToBuy(self, tickets, k):
        t = tickets[k]
        time = 0
        for i, v in enumerate(tickets):
            if i <= k:
                time += min(v, t)
            else:
                time += min(v, t - 1)
        return time

if __name__ == "__main__":
    tickets = list(map(int, input().split()))
    k = int(input())
    print(Solution().timeRequiredToBuy(tickets, k))
