class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:


        """
        The best approach is using histogram
        ["1","0","1","0","0"] ---> [1, 0, 1, 0, 0]
        ["1","0","1","1","1"] ---> [2, 0, 2, 1, 1]
        ["1","1","1","1","1"] ---> [3, 1, 3, 2, 2]
        ["1","0","0","1","0"] ---> [4, 0, 0, 3, 0]

        now after converting each row into histogram we will calculate area for each row
        let's take 3rd row
         0  1  2  3  4
        [3, 1, 3, 2, 2]


        ind     ||      st      ||  area    ||
        0              [0]           0
        1               [1]          3
        2               [1, 2]       3
        3               [1, 3]       3
        4               [1,3,4]      3
        5               []           6
      
        """

        def find_max_area(height):
            area = 0
            st=[]
            m = len(height)

            for j in range(m+1):
                while st and (j == m or height[st[-1]] > height[j]):
                    l = height[st.pop()]
                    w = j if not st else (j - st[-1] - 1)
                    area = max(area, l*w)


                st.append(j) 

            return area


        n, m = len(matrix), len(matrix[0])
        height = [0]*m
        max_area = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    height[j]+=1
                else:
                    height[j] = 0

            ans = find_max_area(height)
            max_area = max(ans, max_area)
        
        return max_area



