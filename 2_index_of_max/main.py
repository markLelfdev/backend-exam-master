"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if numbers is None : return 'list can not blank'
        b = 0
        for i in range(len(numbers)):
            if numbers[i] > b:
                b = numbers[i]
        return f"output = {b}"

solution = Solution()
user_in = input("enter list of numner separated by comma :")
input_list = [int(x) for x in user_in.split(",") if x.strip()]
if not input_list: 
    print('list can not blank')
else : 
    data = solution.find_max_index(input_list)
    print(data)