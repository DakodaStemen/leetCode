class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set('AEIOUaeiou') 
        chars = list(s)  # Convert to list as Strings are immutable
        left = 0  # Pointer 1, start of String
        right = len(s) - 1  # Pointer 2, end of String

        while left < right:  # Two-pointer approach
            while left < right and chars[left] not in vowels: # Move left until vowel is found
                left += 1
            while left < right and chars[right] not in vowels: # Move right until vowel is found
                right -= 1

            # Swap the chars at left and right pointers
            chars[left], chars[right] = chars[right], chars[left]

            left += 1  # Move the pointers inwards from edges
            right -= 1

        return "".join(chars)  # Convert back into a String
