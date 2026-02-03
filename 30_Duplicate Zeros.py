class Solution:
    def duplicateZeros(self, arr):
        n = len(arr)
        zeros = arr.count(0)
        i = n - 1
        j = n + zeros - 1

        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1


def main():
    arr = [1,0,2,3,0,4,5,0]
    sol = Solution()
    sol.duplicateZeros(arr)
    print(arr)


if __name__ == "__main__":
    main()
