class Solution(object):
    def isPalindrome(self, x):
        x = str(x)   #casting
        y = x[::-1]  #reverse of string x is stored in y
        if (x==y):
            return True
        else:
            return False
            
