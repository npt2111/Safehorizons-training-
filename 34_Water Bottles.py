class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        total = 0
        empty = 0
        full = numBottles
        
        while full > 0:
            total += full
            empty += full
            full = empty // numExchange
            empty = empty % numExchange
        
        return total

if __name__ == "__main__":
    numBottles, numExchange = map(int, input().split())
    print(Solution().numWaterBottles(numBottles, numExchange))
