class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return arr
        
        # Process from right to left
        L = n - 2  # Start from second last element
        max_right = arr[n-1]  # Start with last element
        
        # Set last element to -1
        arr[n-1] = -1
        
        while L >= 0:
            # Store current value
            current = arr[L]
            # Replace with max to the right
            arr[L] = max_right
            # Update max_right
            max_right = max(max_right, current)
            L -= 1
        
        return arr

        