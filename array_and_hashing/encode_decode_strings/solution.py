# Time Complexity:
# - encode: O(m) where m is the sum of lengths of all the strings
# - decode: O(m)
# Space Complexity:
# - encode: O(m + n) where n is the number of strings
# - decode: O(m + n)


class Solution:
    @staticmethod
    def encode(strs: list[str]) -> str:
        res = ""
        for string in strs:
            res += f"{len(string)}#{string}"
        return res

    @staticmethod
    def decode(s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            num_end_pos = i
            while s[num_end_pos] != "#":
                num_end_pos += 1
            word_len = int(s[i:num_end_pos])
            res.append(s[num_end_pos + 1 : num_end_pos + 1 + word_len])
            i = num_end_pos + 1 + word_len
        return res


if __name__ == "__main__":
    lists_of_strings = [[""], ["Hello", "World"]]
    for list_of_strings in lists_of_strings:
        assert Solution.decode(Solution.encode(strs=list_of_strings)) == list_of_strings
