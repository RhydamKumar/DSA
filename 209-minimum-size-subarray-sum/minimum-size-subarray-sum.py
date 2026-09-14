class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        rsum = 0
        min_len = float('inf')
        r = 0
        l = 0
        while r<len(nums):
            rsum += nums[r]
            while rsum >= target:
                min_len = min(min_len,r-l+1)
                rsum = rsum- nums[l]
                l +=1
            r +=1
        return 0 if min_len == float('inf') else min_len
