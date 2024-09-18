class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = 0
        right = len(s) - 1
        _max = -1
        res = []
        prev  = 0
        while left < len(s):
            if s[left] != s[right]:
                right -= 1
            elif s[left] == s[right]:
                _max = max(_max, right + 1)
                left += 1
                right = len(s) - 1
                if left == _max:
                    res.append(_max - prev)
                    prev = _max
                    _max = 0
        return res
