class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        end = len(nums1) - 1
        start = 0
        mid = start + (end - start) // 2
        self.mergesort(nums1, start, end)

    def mergesort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        mid = s + (e - s) // 2

        self.mergesort(arr, s, mid)
        self.mergesort(arr, mid + 1, e)

        self.mergearray(arr, s, mid, e)

    def mergearray(self, arr, s, m, e):
        L = arr[s:m+1]
        R = arr[m+1:e+1]

        i, j, k = 0, 0, s

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1