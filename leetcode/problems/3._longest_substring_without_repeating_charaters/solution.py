class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char_map = {}
        start_idx =  0

        for i in range(len(s)):
            if s[i] in char_map and char_map[s[i]] >= start_idx:
                start_idx = char_map[s[i]]+1

            char_map[s[i]] = i
            max_len = max(max_len, i-start_idx+1)
            # print(f"[{i}]: {s[i]=}, {start_idx=}, {char_map=}, {max_len=}")

        return max_len
