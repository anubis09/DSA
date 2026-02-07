# Time Complexity: O(n)
# Space Complexity: O(1) -> only 26 letters in the alphabet


class Solution:
    @staticmethod
    def valid_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        return s_count == t_count


if __name__ == "__main__":
    assert Solution.valid_anagram(s="racecar", t="carrace")
    assert not Solution.valid_anagram(s="jar", t="jam")
