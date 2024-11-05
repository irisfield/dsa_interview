class Solution:
    """438. Find All Anagrams in a String"""

    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        Sliding Window Technique

        The idea is to maintain a sliding window of size len(p) and
        compare the frequency of characters in the window with the
        frequency of characters in string p.
        """
        if len(p) > len(s):
            # If p is longer than s, there cannot be any anagrams
            return []

        # Frequency count for characters in p and in the current window of s
        pCount, sCount = {}, {}

        for i in range(len(p)):  # O(k) time, where k is len(p)
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1

        # Check the first window for anagram
        res = [0] if sCount == pCount else []  # O(k) time

        l = 0
        for r in range(len(p), len(s)):  # O(n) time
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            # Remove the character at the left of the window
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l += 1
            if sCount == pCount:
                res.append(l)
        """
        The time complexity is O(n), where n is the length of s.

        The space complexity is O(1) because s and p consists of lowercase
        English letters, and there are a total of 26 letters in the alphabet.
        This mean that pCount and sCount will use constant additional space.
        """
        return res
