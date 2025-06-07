# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# Input: "abcabcbb"
# Output: 3  # "abc"

# Input: "bbbbb"
# Output: 1  # "b"

# Input: "pwwkew"
# Output: 3  # "wke"

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            print(f"\n[RIGHT = {right}] -> '{s[right]}'")
            while s[right] in seen_chars:
                print(f"  '{s[right]}' already in seen_chars → shrinking window")
                print(f"  Removing '{s[left]}' from seen_chars")
                seen_chars.remove(s[left])
                left += 1
                print(f"  Left pointer now at {left}")

            seen_chars.add(s[right])
            print(f"  Added '{s[right]}' to seen_chars → {seen_chars}")
            # max_length = max(max_length, right - left + 1)
            window_length = right - left + 1
            max_length = max(max_length, window_length)
            print(f"  Current window: '{s[left:right+1]}' → Length: {window_length} | Max: {max_length}")
        print(f"\n✅ Final Max Length: {max_length}")
        return max_length


sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))