class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Step 1:
        # Find how many numbers should exist.
        n = len(nums)

        # Step 2:
        # Compute the expected sum of numbers from 0 to n.
        expected = n * (n + 1) // 2

        # Step 3:
        # Compute the actual sum of the array.
        actual = sum(nums)

        # Step 4:
        # The difference is the missing number.
        return expected - actual