class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        target = n // 4
        count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for char in s:
            count[char] += 1
        if count['Q'] <= target and count['W'] <= target and count['E'] <= target and count['R'] <= target:
            return 0
        
        min_len = n
        left = 0
        for right in range(n):
            count[s[right]] -= 1
            while (left <= right and 
                   count['Q'] <= target and 
                   count['W'] <= target and 
                   count['E'] <= target and 
                   count['R'] <= target):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1
                left += 1
                
        return min_len

        