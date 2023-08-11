class Solution(object):
    def distributeCandies(self, candies, num_people):
        n = num_people
        x = n*(n+1)//2
        if candies > x:
            ans = [i for i in range(1,n+1)]
            remain = candies - x
            y=1
            while remain != 0:
                for j in range(n):            
                    if remain >= (n*y)+j+1:
                        ans[j] += (n*y)+j+1
                        remain -= (n*y)+j+1
                    else:
                        ans[j] += remain 
                        remain = 0
                y+=1                    
        else:
            ans = []            
            for k in range(n):
                if candies >= k+1:
                    ans.append(k+1)
                    candies -= k+1
                else:
                    ans.append(candies)
                    candies = 0                
        return ans


            

