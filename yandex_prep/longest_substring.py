def lengthOfLongestSubstring(s: str) -> int:
    chars = {}
    prev = 0
    max_length = 0
    for cur in range(len(s)):
        if s[cur] in chars and cur >= prev:
            prev = chars[s[cur]] + 1
        chars[s[cur]] = cur
        max_length = max(max_length, cur - prev + 1)
    return max_length


if __name__ == "__main__":
    assert (
        lengthOfLongestSubstring("abcabcbb") == 3
    ), f"Expected 3, got {lengthOfLongestSubstring('abcabcbb')}"
    assert (
        lengthOfLongestSubstring("bbbbb") == 1
    ), f"Expected 1, got {lengthOfLongestSubstring('bbbbb')}"
    assert (
        lengthOfLongestSubstring("pwwkew") == 3
    ), f"Expected 3, got {lengthOfLongestSubstring('pwwkew')}"
    assert (
        lengthOfLongestSubstring("") == 0
    ), f"Expected 0, got {lengthOfLongestSubstring('')}"
    assert (
        lengthOfLongestSubstring("au") == 2
    ), f"Expected 2, got {lengthOfLongestSubstring('au')}"
    assert (
        lengthOfLongestSubstring("dvdf") == 3
    ), f"Expected 3, got {lengthOfLongestSubstring('dvdf')}"
