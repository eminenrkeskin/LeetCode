class Solution:
    def romanToInt(self, s: str) -> int:

        #Created a dictionary for roman numbers
        roman_Dictionary = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        #Created answer variable
        result = 0

        #Created a variable for previous value
        prev_value = 0

        for i in range(len(s) - 1, -1, -1):
            value = roman_Dictionary[s[i]]

            if value < prev_value:
                result -= value
            else:
                result += value

            prev_value = value

        return result
