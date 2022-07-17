class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum ={}
        for i in range(0,len(nums)):
            sum[nums[i]] = i
        for i in range(0,len(nums)):  
            x= target - nums[i]
            if sum.get(x) != None and i != sum[x]:
                return [i , sum[x]]
