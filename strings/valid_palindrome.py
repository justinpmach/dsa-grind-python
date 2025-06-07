# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Input: "A man, a plan, a canal: Panama"
# Output: True

# Input: "race a car"
# Output: False

# Input: " "
# Output: True

class Solution:
    # List Comprehension + join() + isalnum() + lower() - Time: O(n), Space: O(n) 
    # def isPalindrome(self, s: str) -> bool:
    #     cleaned = ''.join([c.lower() for c in s if c.isalnum()])
    #     print('cleaned: ', cleaned)
    #     return cleaned == cleaned[::-1]

    # Two-Pointer Version - Time: O(n), Space: O(1) 
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer if not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer if not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # Move inward
            left += 1
            right -= 1
        return True
    

sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))
# print(sol.isPalindrome("race a car"))
# print(sol.isPalindrome(" "))