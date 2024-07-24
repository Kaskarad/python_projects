class Solution:
    def isValid(self, s: str) -> bool:
        my_open = "([{"
        my_close = {')':'(',']':'[','}':'{'}
        my_check = []
        for i in s:
            if i in my_open:
                my_check.append(i)
            elif len(my_check) > 0:
                if my_close[i] is my_check[-1]:
                    my_check.pop()
                else:
                    break
            else:
                my_check = [1]
                break
        if my_check == []:
            return (True)
        else:
            return (False)
