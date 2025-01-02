class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clear=""
        for i in s:
            if i.isalnum():
                clear+=i.lower()
        l,r=0,len(clear)-1
        while l<r:
            if clear[l]!=clear[r]:
                return False
            l+=1
            r-=1
        return True
        