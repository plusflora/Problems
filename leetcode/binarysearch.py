class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # here we're setting the low and high bounds
        left, right = 0, len(nums)-1
        # as long as we fulfill the conditions of left being <= right we loop through here. find the midpoint (for whatever reason it needs to be left+right)
        # then our primary check is the answer. mid = target. if it's less than the target we increment left up one and do it again. hence why we need to set the mid inside of the while loop. 
        # right side works the same only we subtract one from the index
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

        # I think the best way to do this is to find the middle and search from there.
        # best way to do that is to take the bounds and divide by 2 giving us the middle point of the list. 
        # from there we compare mid to target and with an if statement add or subtract based on if it's higher or lower than the target.