class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        outList = []
        
        for x in nums:
            if x > target:
                return
            elif x <= target:
                for y in nums:
                    if y == target + x:
                        y_index = nums.index(y)
                        outList.append(y_index)
        
        
        print(outList)

inputList1 = [2,7,11,15]
target1 = 9

inputList2 = [3, 2, 4]
target2 = 6

inputList3 = [3, 3]
target3 = 6

Solution.twoSum(0, inputList1, target1)
Solution.twoSum(0, inputList2, target2)
Solution.twoSum(0, inputList3, target3)