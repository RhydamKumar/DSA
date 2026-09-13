class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        l = 0
        r = length-1
        while l<r:
            if numbers[l]+numbers[r] == target :
                return [l+1,r+1]
            elif target > numbers[l]+numbers[r]:
                l +=1
            else:
                r -=1
            