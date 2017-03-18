import random
def selectionsort( aList ):
  for i in range( len( aList ) ):
    least = i
    for k in range( i + 1 , len( aList ) ):
      if aList[k] < aList[least]:
        least = k
 
    swap( aList, least, i )

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

def  createAnArray(size):
    array=[]
    for i in range(0,size):
        array.append(int(random.uniform(-1000,1000)))
        #print(i,".item",array[i])
    return array
size=int(input("size ?"))   
alist=createAnArray(size)
import time
t_start=time.time()
selectionsort(alist)
t_end=time.time()
print("time :",t_end-t_start)

