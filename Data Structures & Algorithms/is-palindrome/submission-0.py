class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        n = len(s)
        left_ptr, right_ptr = 0,n-1

        while left_ptr < right_ptr:
            if s[left_ptr] == s[right_ptr]:
                left_ptr +=1
                right_ptr -= 1
            else:
                return False
        
        return True

        