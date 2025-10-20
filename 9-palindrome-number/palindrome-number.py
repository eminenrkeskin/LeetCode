class Solution: 
    def isPalindrome (self, x):
        original_number = x
        reverse_number= 0

        while x > 0:
            last_number = x % 10

            reverse_number = (reverse_number * 10) + last_number

            x //= 10

        if reverse_number == original_number:
            return True
        else:
            return False

        print(isPalindrome(121))
        print(isPalindrome(-121))
        print(isPalindrome(10))
                
