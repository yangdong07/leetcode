

# 65. Valid Number
# https://leetcode.com/problems/valid-number

class Solution(object):
    def isNumber(self, s):
        try:
            float(s)
            return True
        except:
            return False

import re
class Solution2:
    def isNumber(self, s):
        if re.match(r"^\s*[+-]?(\d+\.\d*|\.?\d+)(e[+-]?\d+)?\s*$", s):
            return True
        return False


class Solution3(object):
    def isNumber(self, s):
        #define a DFA
        states = [
            {},
            # State (1) - initial state (scan ahead thru blanks)
            {'blank': 1, 'sign': 2, 'digit':3, '.':4},
            # State (2) - found sign (expect digit/dot)
            {'digit':3, '.':4},
            # State (3) - digit consumer (loop until non-digit)
            {'digit':3, '.':5, 'e':6, 'blank':9},
            # State (4) - found dot (only a digit is valid)
            {'digit':5},
            # State (5) - after dot (expect digits, e, or end of valid input)
            {'digit':5, 'e':6, 'blank':9},
            # State (6) - found 'e' (only a sign or digit valid)
            {'sign':7, 'digit':8},
            # State (7) - sign after 'e' (only digit)
            {'digit':8},
            # State (8) - digit after 'e' (expect digits or end of valid input)
            {'digit':8, 'blank':9},
            # State (9) - Terminal state (fail if non-blank found)
            {'blank':9}
        ]

        current_state = 1
        for c in s:
            if '0' <= c <= '9':
                c = 'digit'
            elif c == ' ':
                c = 'blank'
            elif c in ['+', '-']:
                c = 'sign'
            if c not in states[current_state].keys():
                return False

            current_state = states[current_state][c]

        if current_state not in [3,5,8,9]:
            return False
        return True

print(Solution3().isNumber('1.'))
print(Solution3().isNumber('abc'))
print(Solution3().isNumber('1 a'))
print(Solution3().isNumber('2e10'))