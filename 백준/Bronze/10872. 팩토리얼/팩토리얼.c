#include <stdio.h>

int main(void)
{
    int count = 0, temp = 1;
    scanf("%d", &count);

    for(int i = 1; i <= count; i++)
    {
        temp = i*temp;
    }

    printf("%d", temp);

    return 0;
}