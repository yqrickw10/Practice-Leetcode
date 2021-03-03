# -*- coding: utf-8 -*-
#2021/03/03 First Try
from typing import List
#stupid solution，brutal force
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]
                
#solution 2: two-pass hash table
    #Idea: build a hash table then check


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        #create hash table
        for index, value in enumerate(nums):
            d[value] = index
        
        print(d)
        
        for index, value in enumerate(nums):
            diff = target - value
            if diff in d:
                if index!=d[diff]:
                    return [index,d[diff]]

#iterate while check, in a loop, first check the hash table, then 
#**Best Solution
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for index, value in enumerate(nums):
            diff = target-value
            if diff not in d:
                d[value] = index
            else:
                return[d[diff],index]

nums=[3,2,4]
target =6
test1 = Solution1()
test2 = Solution2()
test3 = Solution3()

print(test3.twoSum(nums,target))