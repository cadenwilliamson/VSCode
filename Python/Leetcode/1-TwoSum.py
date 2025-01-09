class Solution(object):
    def twoSum(self, givenList : list[int], target : int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        I'm going to attempt a "hash" approach to go through the
        data only once using a dictionary to store the "complements"
        of the `target` and `num` arguments. 
        Giving it a time complexity of O(n), rather
        than brute force, which is O(n^2).
        """
        
        mainDict = {
            "number" : [complement],
        }
        
        print("Original: \n", mainDict)
        
        
        for num in givenList:
            mainDict["number"] += complement
        
        
        for num in givenList:
            mainDict.append(num)
        
        
        
        print("Modified: \n", mainDict)

inputList_1 = [2,7,11,15]
target_1 = 9

inputList_2 = [3, 2, 4]
target_2 = 6

inputList_3 = [3, 3]
target_3 = 6

Solution.twoSum(0, givenList= inputList_1, target= target_1)
Solution.twoSum(0, givenList= inputList_2, target= target_2)
Solution.twoSum(0, givenList= inputList_3, target= target_3)