class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_last = [digits[-1]+1]
        if new_last[0] < 10:
            new_digits = digits[:-1]
            return new_digits + new_last
        else:
            # Last digit was 9, so it becomes 0 (carry over)
            digits[-1] = 0
            # Propagate carry from right to left
            i = len(digits) - 2
            while i >= 0 and digits[i] == 9:
                digits[i] = 0
                i -= 1
            if i >= 0:
                digits[i] += 1
            else:
                digits.insert(0, 1)
        return digits
