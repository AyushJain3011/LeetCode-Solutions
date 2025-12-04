def longSubarrWthSumDivByK (self,arr,  n, k) : 
		#Complete the function
		d={};
		d[0]=0;
		s = 0;
		ans = 0
		for i in range(n):
		  #  neg = False
		    
		    s = s+(arr[i]%k)%k;
		  #  print(s)
		    if s in d:
		        ans= max(ans, i-d[s]+1);
		    else:
		        d[s] = i+1;
		        


        return ans