def removeElement(self, nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i
x =removeElement(None,[2,2,2,3,4,5,2,2],2)
print(x)


        
    