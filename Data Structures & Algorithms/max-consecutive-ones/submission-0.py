class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = res = 0
        for val in nums:
            if val == 1:
                counter += 1
            else:
                res = max(counter, res)
                counter = 0
        res = max(counter, res)
        
        return res
