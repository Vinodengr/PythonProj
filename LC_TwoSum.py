class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# Approach -1 
#        for i in range(len(nums)):
#            for j in range(i+1, len(nums)):
#                if target == nums[i]+ nums[j]:
#                    return [i,j]


# Approach - 2
        num_dict ={}            
        for i, num in enumerate(nums):
            x = target - num
            if x in num_dict:
                return [num_dict[x],i]
            else:                
                num_dict[num] = i              
        
        return[]


x = Solution.twoSum(None,[2,7,11,15],19)

