class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
    
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    print(sol.containsDuplicate(nums1))  
    print(sol.containsDuplicate(nums2)) 
    print(sol.containsDuplicate(nums3))  
