class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        lis = [''] * len(s)
        while left <= right:
            if s[left] not in vowels:
                lis[left] = s[left]
                left += 1
            elif s[left] in vowels and s[right] not in vowels:
                lis[right] = s[right]
                right -= 1
            elif s[left] in vowels and s[right] in vowels:
                lis[left] = s[right]
                lis[right] = s[left]
                left += 1
                right -= 1
        return "".join(lis)
