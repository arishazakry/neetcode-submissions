class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res = []
        two_zeros_flag = 0
        for i in nums:
            prod = prod * i
            if i == 0:
                two_zeros_flag += 1
        for i in range(len(nums)):
            if nums[i]:
                x = prod // nums[i]
            elif two_zeros_flag > 1:
                x = 0
            else:
                x = 1
                for num in range(len(nums)):
                    if num != i:
                        x = x * nums[num]
            res.insert(i, x)
        return res

        