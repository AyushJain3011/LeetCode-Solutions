class Solution:
    def isNumber(self, s: str) -> bool:
        """
        There can be only one decimal

        
        """
        is_decimal = False
        number_seen = False

        i = 0
        if s[i] in ['-', '+']:
            i+=1

        while i < len(s):

            curr_char = s[i]
            if curr_char.isalpha():
                if curr_char not in ['e', 'E']:
                    return False
                else:
                    return number_seen and self.is_integer(s[i+1:])

            elif curr_char in ['-', '+']:
                return False

            elif curr_char == '.':
                if is_decimal:
                    return False
                else:
                    is_decimal = True

            else:
                number_seen = True

            i+=1

        return number_seen

    def is_integer(self, string):
        "if string is empty"
        if not string:
            return False
        
        number_seen = False
        i = 0

        # there can be a sign
        if string[0] in ['-', '+']:
            i+=1
        
        while i < len(string):
            curr_char = string[i]

            if curr_char.isalpha():
                return False
            elif curr_char in ['-', '+']:
                return False
            elif curr_char == '.':
                return False
            else:
                number_seen = True
            
            i+=1
        
        return number_seen

        











