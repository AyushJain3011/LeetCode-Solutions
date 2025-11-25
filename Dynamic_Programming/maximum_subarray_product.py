class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        """
        -ve * -ve = +ve
        at any point if our product is -ve and we multipy by -ve number than we get the max_prduct

        so there is higher chances that when we multiply by -ve number our prev_product must be -ve than we can get the higest number

        so what we can do take two var
        max_pro, min_pro
        if num < 0 :
            swap(min_pro, max_pro)

        """
        n = len(nums)

        if n == 1:
            return nums[0]

        ans = float('-inf')
        min_pro, max_pro, ans = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            if num < 0:
                min_pro, max_pro = max_pro, min_pro
        
            min_pro = min(num, min_pro*num)
            max_pro = max(num, max_pro*num)

            ans = max(ans, max_pro)

        return ans


        

            