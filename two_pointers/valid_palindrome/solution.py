# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    assert Solution.is_palindrome("Was it a car or a cat I saw?")
    assert not Solution.is_palindrome("tab a cat")
