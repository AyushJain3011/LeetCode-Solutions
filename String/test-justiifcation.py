class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        # if maxWidth == 1:
        #     s = ""
        #     return list([s+words[i] for i in range(len(words))])
        
        n = len(words)
        temp = []
        i = 0
        str_len = []

        # partition the character in diffrent list
        while i < n:
            curr_leng = 0
            li = []
            while i<n:
                if curr_leng + len(words[i]) > maxWidth:
                    curr_leng -= 1
                    break
                
                
                curr_leng += len(words[i]) + 1

                li.append(words[i])
                i+=1

            str_len.append(curr_leng)
            temp.append(li)
        
        # joining the list 
        ans = []
        for i, li in enumerate(temp):
            letters = sum(len(word) for word in li)

            string = ""
            diff = maxWidth - str_len[i]

            if i == len(temp) - 1:
                s = " ".join(li)
                string = s.ljust(maxWidth)

            else:
                
                if len(li) == 1:
                    string = li[0].ljust(maxWidth)
                   
                else:
                    total_spaces = maxWidth - letters
                    gaps = len(li) - 1

                    # distributning extra space from the left side
                    space_per_gap = total_spaces // gaps  # minimum space which will be distribute b/w cahracter
                    extra_spaces = total_spaces % gaps  # extra space which will be addes from the left to right

                    string = ""
                    for i in range(gaps):
                        string += li[i]
                        string += " " * (space_per_gap + (1 if i < extra_spaces else 0))
                    string += li[-1]

                    
            ans.append(string)

        return ans






