class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        total_substrings = 0
        left = 0
        counts = { '0': 0, '1': 0 }
        for right in range(len(s)):
            counts[s[right]] += 1
            while counts['0'] > k and counts['1'] > k:
                counts[s[left]] -= 1
                left += 1
            total_substrings += (right - left + 1)
            
        return total_substrings

