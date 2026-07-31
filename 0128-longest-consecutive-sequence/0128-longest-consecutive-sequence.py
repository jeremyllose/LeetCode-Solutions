class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#  Step 1:
# Create a fast lookup containing every number.
        num_set = set(nums)
        longest = 0
# Step 2:
# For each number in the input:
        for num in num_set:
#     Check whether it is the beginning of a consecutive chain.
            if num - 1 not in num_set:
#     If it is the beginning:

#         Start counting the chain length.
                current = num
                length = 1
                

                while current + 1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest
#         Continue checking if the next consecutive number exists.

#         Stop when the next number no longer exists.

# Step 3:
# Compare the chain length with the longest chain found so far.
            
# Step 4:
# Return the longest chain length.
            
