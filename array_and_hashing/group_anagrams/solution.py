from collections import defaultdict

# Time complexity O(n*m) where n is tht len of the input and m the len of the longest string.
# Space complexity O(n*m)


class Solution:
    @staticmethod
    def group_anagrams(strs: list[str]) -> list[list[str]]:
        anagrams_hash_map = defaultdict(list)
        for string in strs:
            counter = [0] * 26
            for char in string:
                index = ord(char) - ord("a")
                counter[index] += 1
            # we need an immutable type for hashing (tuple or string)
            anagrams_hash_map[tuple(counter)].append(string)
        return list(anagrams_hash_map.values())


if __name__ == "__main__":
    assert Solution.group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"]) == [
        ["act", "cat"],
        ["pots", "tops", "stop"],
        ["hat"],
    ]
    assert Solution.group_anagrams(["x"]) == [["x"]]
    assert Solution.group_anagrams([""]) == [[""]]
