class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums) == 0):
            return -1
        if(len(nums) == 1):
            if (nums[0] == target):
                return 0
            return -1
        copy = nums
        run = True
        start = 0
        cap = len(nums)-1
        count = 0
        middle = math.ceil((cap + start)/2)
        prevMiddle = None
        while(run):
           
            middle = math.ceil((cap + start)/2)
            if (nums[middle] > nums[cap]):
                start = middle
                
            elif(nums[start] > nums[middle-1]):
                cap = middle
            count = count + 1
            if (nums[middle-1] > nums[middle]):
                run = False
            if (prevMiddle == middle):
                run = False
            print(middle)
            prevMiddle = middle
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
print(x.search([1,2], 0))