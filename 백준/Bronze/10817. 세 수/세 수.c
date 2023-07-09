#include <stdio.h>
int main() {
    int a, b, c, min;
    scanf("%d %d %d", &a, &b, &c);
    min = a;
    if (min > b)    min = b;
    if (min > c)    min = c;
    
    if (min == a){
        if (b <= c)        printf("%d", b);
        else    printf("%d", c);
    }
    else if (min == b){
        if (a <= c)        printf("%d", a);
        else    printf("%d", c);
    }
    else{
        if (a <= b)        printf("%d", a);
        else    printf("%d", b);
    }
   return 0;
}