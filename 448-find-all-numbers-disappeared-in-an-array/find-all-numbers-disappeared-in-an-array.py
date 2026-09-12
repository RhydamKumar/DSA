class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        set2= set()
        length = len(nums)
        for i in range(1,length+1):
            if i not in set1:
                set2.add(i)
        l1 = list(set2)
        return l1


