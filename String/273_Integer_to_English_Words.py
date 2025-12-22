class Solution:
    def numberToWords(self, num: int) -> str:
        units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def convert(n):
            nonlocal units, teens, tens
            if 0 < n < 9:
                return units[n]
            elif 10 <= n <= 19:
                return teens[n-10]
            else:
                s = ""
                s = tens[n//10]
                if s and n%10:
                    s += " "
                return  s + (units[n%10] if n%10 > 0 else "")


        if num == 0: return 'Zero'
        unit=["", ' Thousand', ' Million', ' Billion']
        N = str(num)
        n = len(N)
        word = ""
        cnt = 0

        for i in range(n, -1, -3):
            if i == 0:
                break
            st = i-3 if i-3 >= 0 else 0
            nums = N[st:i]
            string = ""
            
            string = units[int(nums)//100] + ' Hundred' if int(nums)//100 else ""

            if string and int(nums)%100: 
                string += " "

            string = string + (convert(int(nums)%100) if int(nums)%100 else "")

            # if not empty string
            if string:
                string += unit[cnt]
                # if not empty word 
                if word:
                    string += " "

          
            word = string + word
            cnt += 1

        return word





            


        
        