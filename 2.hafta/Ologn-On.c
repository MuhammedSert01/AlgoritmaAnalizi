#include <stdio.h>
#include <stdlib.h>

int step=0;

int pow(int x, int y){
    int us=1;
    int i;
    for (i=0;i<y;i++){
        us=us*x;
    }
    return us;
}
long LongPow(int x,int n)
{
     step++;
    if(n==0) return 1;
    if(n==1) return x;
    if(n%2==0)
        return LongPow(x*x,n/2);
    else
        return LongPow(x*x,n/2)*x;
}

int main()
{

   int taban=5;
   int ust=3;

   printf("\nsonuc:%d",pow(taban,ust));
   printf("\nsonuc:%d step:%d",LongPow(taban,ust),step);


  system("PAUSE");
    return 0;
}
