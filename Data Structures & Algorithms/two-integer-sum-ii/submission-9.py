class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            while numbers[l] == numbers[l + 1]:
                l += 1

            while numbers[r] == numbers[r - 1]:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1

            elif numbers[l] + numbers[r] > target:
                r -= 1


            else:
                return [l + 1, r + 1]

            


        