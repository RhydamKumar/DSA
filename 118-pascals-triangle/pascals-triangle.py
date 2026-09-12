class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        num_list=[[1],[1,1]]
        prev_row = [1,1]
        nums = [1]
        for row in range (2,numRows):
            for elem in range(1,row):
                item  = prev_row[elem] + prev_row[elem-1]
                nums.append(item)
            nums.append(1)
            prev_row = nums
            num_list.append(nums)
            nums = [1]
        if not (numRows > 1):
            return [[1]]
        return num_list






        