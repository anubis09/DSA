# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    @staticmethod
    def contains_duplicates(nums: list[int]) -> bool:
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False

    @staticmethod
    def other_sol(nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)


if __name__ == "__main__":
    assert Solution.contains_duplicates([1, 2, 3, 3])
    assert not Solution.contains_duplicates([1, 2, 3, 4])
