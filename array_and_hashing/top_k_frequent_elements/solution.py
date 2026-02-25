# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    @staticmethod
    def top_k_freq(nums: list[int], k: int) -> list[int] | None:
        freq_counter = {}
        # +1 because if I have [3,3] i need freq[2] available
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            freq_counter[n] = freq_counter.get(n, 0) + 1
        for n, freq in freq_counter.items():
            freq_buckets[freq].append(n)

        out = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                out.append(n)
                if len(out) == k:
                    return out


if __name__ == "__main__":
    assert Solution.top_k_freq([1, 2, 2, 3, 3, 3], 2) == [3, 2]
    assert Solution.top_k_freq([7, 7], 1) == [7]
