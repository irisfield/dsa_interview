class Solution:
    """383. Ransom Note"""

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Intuition:
        Count the frequencies of all the characters in magazine.
        Iterate through the characters in the ransom note.
        Decrement the count of the characters in the hash map, and
        return false if it ever reaches zero for any character.
        """
        count = {}

        for c in magazine:  # O(n) time and space
            count[c] = count.get(c, 0) + 1

        for c in ransomNote:  # O(m) time
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1

        """
        The time complexity: O(m + n), where m is the length of
        ransomNote and n is the length of magazine.

        The space complexity is O(n), where n is the length of magazine.
        """
        return True
