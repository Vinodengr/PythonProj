def count_rotations_binary(nums):
    lo = 0
    hi = 

    while lo<hi:
        mid = (lo + hi)//2
        mid_number = nums[mid]

        if mid>0:
            return mid
        elif mid_number > nums[hi]:
            lo = mid+1
        elif mid_number < nums[hi]:
            hi = mid
    return -1

