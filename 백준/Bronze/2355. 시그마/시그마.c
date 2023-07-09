#include <stdio.h>

int main(void)
{
    long long a, b, temp = 0;

    scanf("%lld %lld", &a, &b);

    if (a > b)
    {
        temp = a;
        a = b;
        b = temp;
    }

    temp = (a + b) * (b - a + 1) / 2;

    printf("%lld", temp);

    return 0;
}
