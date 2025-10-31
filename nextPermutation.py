class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Find the pivot index
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # If a pivot exists
        if i >= 0:
            # Find successor from the right that's larger than the pivot
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap them
            nums[i], nums[j] = nums[j], nums[i]
        # Reverse the suffix after the pivot
        nums[i+1:] = reversed(nums[i+1:])


        
