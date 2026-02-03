from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        
        for h, e in zip(heights, expected):
            if h != e:
                count += 1
        
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.heightChecker([1,1,4,2,1,3]))  # 3
    print(sol.heightChecker([5,1,2,3,4]))    # 5
    print(sol.heightChecker([1,2,3,4,5]))    # 0
