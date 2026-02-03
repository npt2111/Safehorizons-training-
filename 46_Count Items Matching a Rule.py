class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        m = {"type": 0, "color": 1, "name": 2}
        idx = m[ruleKey]
        c = 0
        for it in items:
            if it[idx] == ruleValue:
                c += 1
        return c

if __name__ == "__main__":
    n = int(input().strip())
    items = []
    for _ in range(n):
        items.append(input().split())
    ruleKey = input().strip()
    ruleValue = input().strip()
    print(Solution().countMatches(items, ruleKey, ruleValue))
