class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            
            while j < k:
                sum_three = nums[i] + nums[j] + nums[k]
                if sum_three > 0:
                    k -= 1
                elif sum_three < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1


        return result


        