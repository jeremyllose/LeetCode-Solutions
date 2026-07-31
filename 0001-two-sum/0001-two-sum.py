class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i

# Algorithm:

# For each number in the array:

#     Choose the current number (candidate i).

#     Compute the value needed to reach the target.
#     needed = target - current number

#     If the needed value has already been seen,
#         return [index of needed value, current index]

#     Otherwise,
#         remember the current number and its index.

# Continue until the answer is found.