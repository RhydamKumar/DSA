class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left =0
        right = 0 
        length = len(nums)-1
        for i in range(0,length+1):
            right = 0
            right = total-left-nums[i]
            if right == left :
                return i               
            left = left + nums[i]
        return -1




        