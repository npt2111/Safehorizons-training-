class Solution:
    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, l, r):
        if l >= r:
            return

        m = (l + r) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m + 1, r)
        self.merge(nums, l, m, r)

    def merge(self, nums, l, m, r):
        left = nums[l:m+1]
        right = nums[m+1:r+1]

        i = j = 0
        k = l

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArray([5,2,3,1]))
    print(sol.sortArray([5,1,1,2,0,0]))
