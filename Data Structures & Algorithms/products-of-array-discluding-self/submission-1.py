class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        backward = []
        a = 1
        for i in range(len(nums)):
            forward.insert(i, a)
            a *= nums[i]
        a = 1
        for i in range(len(nums) - 1, -1, -1):
            backward.insert(0, a)
            a *= nums[i]
        res = []
        for i in range(len(nums)):
            res.insert(i, backward[i] * forward[i])
        return res
            