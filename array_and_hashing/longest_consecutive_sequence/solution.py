class Solution:
    @staticmethod
    def longest_sequence(nums: list[int]) -> int:
        lookup = set(nums)
        longest_sequence = 0
        for n in nums:
            if n - 1 not in lookup:
                # this is the possible start of a sequence
                curr_length = 1
                while n + curr_length in lookup:
                    curr_length += 1
                longest_sequence = max(longest_sequence, curr_length)
        return longest_sequence


if __name__ == "__main__":
    assert Solution.longest_sequence([2, 20, 4, 10, 3, 4, 5]) == 4
    assert Solution.longest_sequence([0, 3, 2, 5, 4, 6, 1, 1]) == 7
    assert Solution.longest_sequence([0]) == 1
    assert Solution.longest_sequence([]) == 0
