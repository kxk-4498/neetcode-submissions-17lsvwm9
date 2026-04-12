class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        tmp = 0
        for i in nums:
            if i == 1:
                tmp += 1
            else:
                counter = max(counter, tmp)
                tmp = 0
        counter = max(counter, tmp)
        return counter 
