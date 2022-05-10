# Least Larger
# Given an array of numbers and an index, return the index of the least number
# larger than the element at the given index, or -1 if there is no such index.
# Example:
# Input: ([4, 1, 3, 5, 6], 0 ) 
# Output: 3
# Input: ([4, 1, 3, 5, 6], 4)
# Output: -1




def leastLarger(nums, i):
    # higher = []
    # for n in nums:
    #     if n > nums[i]:
    #         higher.append(n)
    higher= [n for n in nums if n > nums[i]]
    if higher:
        return nums.index(min(higher))
    return -1
print(leastLarger([4, 1, 3, 5, 6], 0))