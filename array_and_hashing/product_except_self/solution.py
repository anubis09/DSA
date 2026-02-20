# Time Complexity O(n)
# Space Complexity O(n)


class Solution:
    @staticmethod
    def product_except_self(nums: list[int]) -> list[int]:
        # pre-computing stage
        length = len(nums)
        prefix = [1] * length
        for i in range(1, length):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        suffix = [1] * length
        for i in range(length - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        res = []
        for i in range(length):
            res.append(prefix[i] * suffix[i])
        return res

    @staticmethod
    def no_additional_space_solution(nums: list[int]) -> list[int]:
        length = len(nums)
        res = [1] * length
        accumulator = 1
        for i in range(length):
            res[i] *= accumulator
            accumulator *= nums[i]
        accumulator = 1
        for i in range(length - 1, -1, -1):
            res[i] *= accumulator
            accumulator *= nums[i]
        return res


if __name__ == "__main__":
    assert Solution.product_except_self([1, 2, 4, 6]) == [48, 24, 12, 8]
    assert Solution.product_except_self([-1, 0, 1, 2, 3]) == [0, -6, 0, 0, 0]

    assert Solution.no_additional_space_solution([1, 2, 4, 6]) == [48, 24, 12, 8]
    assert Solution.no_additional_space_solution([-1, 0, 1, 2, 3]) == [0, -6, 0, 0, 0]
