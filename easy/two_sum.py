class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    sumDict = {}
    i = 0
    for num in nums:
      val = target - num
      if (num not in sumDict):
        sumDict[val] = i
      else: 
        return [sumDict[num], i]        
      i = i + 1

