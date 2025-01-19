class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Two–pointer approach

        # Initialize pointers
        p1 = m - 1 # Pointer for the last valid element in nums1
        p2 = n - 1 # Pointer for the last element in nums2
        p = m + n - 1 # Pointer for the last position in nums1

        # Traverse nums1 and nums2 from the back and fill nums1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        