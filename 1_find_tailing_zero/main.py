"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:
    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0 :
            return "number can not be negative"
        else :
            count = 0 # สร้างเพื่อเก็บตัวประกอบเลข 5 
            power = 5 # เพื่อเก็บจำนวนที่นำ 5 ไปคูณเช่น 5,25,125
            while number // power >= 1 : # เข้าเงื่อนไขเมื่อ หารแล้วไม่เท่ากับ 0 
                count += number // power
                power *= 5
            return f"output = {count}"

    
    def factorial(self,number : int) -> int | str :
        if number == 0 or number == 1:
            return 1
        else :
            return number * self.factorial(number -1 )
        
    def find_tail (self,factorial : int) -> int | str :
        count = 0
        while factorial % 10 == 0:
            count += 1
            factorial = factorial // 10
        return count
                 

solution = Solution()
user_in = input("enter number to factorial :")
if not user_in: 
    print('please enter a number')
else : 
    fac = solution.factorial(int(user_in))
    print(solution.factorial(int(user_in)))
    print(solution.find_tail(int(fac))) 
    print(solution.find_tailing_zeroes(int(user_in)))

