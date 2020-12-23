class Solution:

    def searchInsert(self, nums, target):
        lo = 0
        hi = len(nums)

        while (lo <= hi):
            mid = (lo + hi)//2

            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 4, 5, 6]
    target = 7
    print(s.searchInsert(nums, target))
