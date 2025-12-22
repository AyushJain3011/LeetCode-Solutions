  class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Take two poiner slow and fast and loop until slow == Fast
        
        """
        def sum_sq_digits(n):
            
            num = 0
            while n:
                rem = n%10
                num += rem*rem
                n//=10

            return num

        slow = n
        fast = sum_sq_digits(n)

        while slow != fast:
            slow = sum_sq_digits(slow)
            fast = sum_sq_digits(fast)
            fast = sum_sq_digits(fast)
        
        if sum_sq_digits(fast) == 1:
            return True
        return False


# we can also use a set to check if number occure in past or not 

        

        



        