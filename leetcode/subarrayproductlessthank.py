class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding window style problem
        N = len(nums)
        # 
        total = 0
        product = 1
        left = 0
        for right in range(N):
            product *= nums[right]

            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            
            total += max(right - left + 1, 0)
        return total
