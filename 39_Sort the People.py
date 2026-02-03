class Solution:
    def sortPeople(self, names, heights):
        return [n for _, n in sorted(zip(heights, names), reverse=True)]

if __name__ == "__main__":
    names = input().split()
    heights = list(map(int, input().split()))
    print(Solution().sortPeople(names, heights))
