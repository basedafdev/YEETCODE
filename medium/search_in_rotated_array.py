import math
from bisect import bisect_left 

class Solution:
    def search(self, nums, target):
        copy = nums
        run = True
        start = 0
        cap = len(nums)-1
        count = 0
        middle = math.ceil((cap + start)/2)
        while(run):
            middle = math.ceil((cap + start)/2)
            if (nums[middle] > nums[cap]):
                start = middle
            elif(nums[start] > nums[middle-1]):
                cap = middle
            count = count + 1
            if (nums[middle-1] > nums[middle]):
                run = False
        search = True
        mid = middle
        
        start = 0
        end = mid-1
        if (nums[mid] <= target <= nums[len(nums)-1]):
            start = mid 
            end = len(nums)-1
            
        while start <= end: 
            mid = int(start + (end - start)/2); 
            
            if nums[mid] == target: 
                return mid 
    
            elif nums[mid] < target: 
                start = mid + 1
    
            else: 
                end = mid - 1
        return -1
        

x = Solution()
print(x.search([3,1], 0))