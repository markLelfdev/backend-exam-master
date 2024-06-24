"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number < 1 or number > 3999  :
            return ("number can't be less than 1 or more than 3999")
        else :
            roman = ""
            roman_dict =  {1000:"M",900:"CM",500:"D"
                           ,400:"CD",100:"C",90:"XC",50:"L"
                           ,40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
            for key in sorted(roman_dict.keys(),reverse=True):
                while number >= key:
                    roman += roman_dict[key]
                    number -= key
            return (roman)
    
solution = Solution()
user_in = input("enter number to roman :")
if not user_in: 
    print('please enter a number')
else : 
    print(solution.number_to_roman(int(user_in)))