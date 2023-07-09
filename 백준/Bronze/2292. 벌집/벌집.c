#include <stdio.h>

int main(void)
{
    int num, result = 1, cnt = 1, temp = 1;

    scanf("%d", &num);

    if (num != 1)
    {
        while (temp < num)
        {
            temp += 6 * cnt;
            cnt += 1;
        }
        result = cnt;
    }

    printf("%d", result);

    return 0;
}