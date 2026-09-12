class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num1 = int(''.join(map(str,digits)))
        final_num = num1 + 1
        result = list(map(int,str(final_num)))
        return result
