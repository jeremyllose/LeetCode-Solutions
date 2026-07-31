class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Step 1:
        # Remove all non-alphanumeric characters.
        # Code:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char

        # Step 2:
        # Convert all letters to lowercase.
        # Code:
        cleaned = cleaned.lower()

        # Step 3:
        # If the cleaned string is empty,
        #     return True.
        # Code:
        if cleaned == "":
            return True

        # Step 4:
        # Reverse the cleaned string.
        # Code:
        reversed_string = cleaned[::-1]

        # Step 5:
        # If the reversed string is the same as the cleaned string,
        #     return True.
        # Otherwise,
        #     return False.
        # Code:
        if cleaned == reversed_string:
            return True
        else:
            return False