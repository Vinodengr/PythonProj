class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                print("low:" ,lo)
                print("High:" , hi)
                mid = (lo+hi)//2
                print("mid", mid)
                if nums[mid] < x:
                    lo = mid +1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:        
            return [lo, hi]
                
        return [-1, -1]

x= Solution.searchRange(None,[5,7,7,8,8,10],8)
print(x)