class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        l1 = []
        length = len(nums)
        for i in range(1,length+1):
            if i not in set1:
                l1.append(i)
        return l1


