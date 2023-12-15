class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        e =[]
        if x <0:
            return False
        else:
            while x>0:
                x, rd = divmod(x,10)
                e.append(rd)
            a=e[::-1]
            if a == e:
                return True
            else:
                return False

        