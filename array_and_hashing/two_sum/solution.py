class Solution:
    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        diff_map = {}  # target-n -> index
        for i, n in enumerate(nums):
            diff_index = diff_map.get(n, None)
            if diff_index is not None:
                return [diff_index, i]
            else:
                diff_map[target - n] = i
        return [-1, -1]


if __name__ == "__main__":
    assert Solution.two_sum(nums=[3, 4, 5, 6], target=7) == [0, 1]
    assert Solution.two_sum(nums=[4, 5, 6], target=10) == [0, 2]
    assert Solution.two_sum(nums=[5, 5], target=10) == [0, 1]
