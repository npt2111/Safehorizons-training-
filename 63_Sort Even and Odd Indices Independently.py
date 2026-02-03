class Solution:
    def sortEvenOdd(self, nums):
        even = sorted(nums[0::2])         
        odd = sorted(nums[1::2], reverse=True) 
        
        e = o = 0
        res = []
        
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(even[e])
                e += 1
            else:
                res.append(odd[o])
                o += 1
        return res


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().sortEvenOdd(nums))
