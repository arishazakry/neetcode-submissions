class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []
        
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            ptr1 = i + 1
            ptr2 = len(nums) - 1
            while (ptr1 < ptr2):
                sum = num + nums[ptr1] + nums[ptr2]
                if sum == 0:
                    if [num, nums[ptr1], nums[ptr2]] not in res:
                        res.append([num, nums[ptr1], nums[ptr2]])
                    ptr1 += 1
                    ptr2 -= 1
                if sum > 0:
                    ptr2 -= 1
                if sum < 0:
                    ptr1 += 1
        
        return res
            
