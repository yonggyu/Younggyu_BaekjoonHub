#include <stdio.h>

int main(void)
{
    int a, b;
    double temp;

    scanf("%d", &a);
    scanf("%d", &b);

    temp = (2 * a) + (2 * b) * 3.141592;

    printf("%lf", temp);

    return 0;
}