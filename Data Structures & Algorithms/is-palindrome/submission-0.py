class Solution:
    def expand_from_center(self, left: int, right: int, s: str) -> tuple[int, int]:
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        return (left, right)

    def isPalindrome(self, s: str) -> bool:
        clean = "".join([c.lower() for c in s if c.isalnum()])
        n = len(clean)
        if n == 0:
            return True
        if n % 2 == 1:
            middle = n // 2
            left, right = self.expand_from_center(middle, middle, clean)
        else:
            middle = n // 2
            left, right = self.expand_from_center(middle -1, middle, clean)
        return left == -1 and right == n
