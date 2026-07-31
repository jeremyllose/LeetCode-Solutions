class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #Question is basically telling us to output the reverse of a string
        #first lets call the list first? make it remember the position that matters here not really the length HOW THOUGH?
        #second reverse the string by calling the end of the string, second to the last
        #release second as output
        left = 0

        right = len(s)-1

        while left < right:
            # swap
            s[left], s[right] = s[right], s[left]
            # move left
            left += 1
            # move right
            right -= 1