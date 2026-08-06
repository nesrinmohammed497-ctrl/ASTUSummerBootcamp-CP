class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = right = k
        minimum = nums[k]
        ans = minimum
        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
            else:
                right += 1
            minimum = min(minimum, nums[left], nums[right])
            ans = max(ans, minimum * (right - left + 1))
        return ans
        