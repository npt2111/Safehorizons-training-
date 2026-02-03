class Solution:
    def countHillValley(self, nums):
        arr = [nums[0]]
        for x in nums[1:]:
            if x != arr[-1]:
                arr.append(x)
        c = 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                c += 1
            elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                c += 1
        return c


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().countHillValley(nums))
