#include <stdio.h>

int main(void)
{
    int count = 0;
    scanf("%d", &count);
    int num[count];
    int max = 0;
    int min = 0;
    
    for(int i = 0; i < count; i++)
    {
        scanf("%d", &num[i]);
    }
    
    max = num[0];
    min = num[0];
    
    for(int i = 1; i < count; i++)
    {
        if(num[i] > max){
            max = num[i];
        }
        if(num[i] < min){
            min = num[i];
        }
    }
    
    printf("%d %d", min, max);

    return 0;
}