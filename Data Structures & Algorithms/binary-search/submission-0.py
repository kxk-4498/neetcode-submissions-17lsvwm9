class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1  # Fix: e should be len(nums)-1
    
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m + 1
            else:  # nums[m] > target
                e = m - 1
        
        return -1

        