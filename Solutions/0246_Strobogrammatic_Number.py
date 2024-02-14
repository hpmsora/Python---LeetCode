class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        exchange_dict = {
            "1" : "1",
            "6" : "9",
            "8" : "8",
            "9" : "6",
            "0" : "0"
        }

        same_dict = {
            "1" : "1",
            "8" : "8",
            "0" : "0"
        }

        if len(num) % 2 == 1:
            if not num[len(num)//2] in same_dict:
                return False
        
        for index in range(len(num)//2):
            curr_num = num[index]

            if not curr_num in exchange_dict:
                return False
            
            exc_num = num[len(num) - index - 1]
            if not exc_num in exchange_dict:
                return False
            
            if not curr_num == exchange_dict[exc_num]:
                return False
        
        return True
