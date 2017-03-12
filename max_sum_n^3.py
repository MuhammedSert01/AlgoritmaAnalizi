import random 
import timeit

def maxSubSum(array): 
     maxSum=0 
     for i in range(0,len(array)): 
         for j in range(i,len(array)): 
             thisSum=0 
             for k in range(i,j): 
                 thisSum=thisSum+array[k] 
             if(thisSum>maxSum): 
                 maxSum=thisSum 
     return maxSum 
  
size=int(input("dizinin boyutu ne olsun : ")) 
array=[] 
for i in range(0,size): 
     array.append(random.randint(-20,20))  

import time 
start_time=time.time() 
print("maxSubSum1 sonucu :", maxSubSum(array)) 
print("gecen süre : ", time.time()-start_time) 


