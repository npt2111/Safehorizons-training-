class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            
if __name__ == "__main__":
    sol = Solution()
    # Test case 1
    nums = [2, 7, 11, 15]
    target = 9
    print("Input:", nums, "Target:", target)
    print("Output:", sol.twoSum(nums, target))  # [0, 1]

    # Test case 2
    nums = [3, 2, 4]
    target = 6
    print("Input:", nums, "Target:", target)
    print("Output:", sol.twoSum(nums, target))  # [1, 2]

    # Test case 3
    nums = [3, 3]
    target = 6
    print("Input:", nums, "Target:", target)
    print("Output:", sol.twoSum(nums, target))  # [0, 1]
