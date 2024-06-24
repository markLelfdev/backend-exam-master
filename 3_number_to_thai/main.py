"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        digit = ['','สิบ','ร้อย','พัน','หมื่น','แสน','ล้าน','สิบล้าน']
        noun =['','หนึ่ง','สอง','สาม','สี่','ห้า','หก','เจ็ด','แปด','เก้า']
        
        if number < 0 : return('number can not less than 0')
        elif number == 0 : return('ศูนย์')
        else : 
            number_str = str(number)
            data_len = len(number_str)
            word = ""
        for i,digit_n in enumerate(number_str):
            # print(i,digit_n)
            num = int(digit_n)
            place = data_len - i - 1
            # print(num, place)
            
            if num != 0:
                if place == 1 and num == 1:
                    word = word + digit[1]
                elif place == 1 and num == 2 :
                    word = word + "ยี่สิบ"
                elif place == 0 and num == 1 :
                    word = word + "เอ็ด"
                else :
                    word += noun[num] + digit[place]
            else :
                continue
        return word

solution = Solution()
user_in = input("enter number to thai :")
if not user_in: 
    print('please enter a number')
else : 
    print(solution.number_to_thai(int(user_in)))
