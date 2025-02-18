'''
242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Examples
1. Input: s = 'anagram', t = 'nagaram'
Output: true

2. Input: s = 'rat', t = 'car'
Output: false
You may assume the string contains only lowercase alphabets.
'''


def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


def is_anagram_v2(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    _freqs, _freq2 = {}, {}

    for c in s1:
        _freqs[c] = _freqs.get(c, 0) + 1

    for c in s2:
        _freq2[c] = _freq2.get(c, 0) + 1

    for c in _freqs:
        if c not in _freq2 or _freqs[c] != _freq2[c]:
            return False

    return True


assert is_anagram('anagram', 'nagaram') == True
assert is_anagram('rat', 'car') == False
