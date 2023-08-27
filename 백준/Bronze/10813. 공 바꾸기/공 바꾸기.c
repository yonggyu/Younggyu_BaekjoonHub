#include <stdio.h>

int main(void)
{
    int n, m;
    scanf("%d %d" , &n, &m);

    int a[101];
    for (int i = 1; i <= n; i++)
    {
        a[i] = i;
    }

    int num1, num2;
    for (int i = 0; i < m; i++)
    {
        scanf("%d %d", &num1, &num2);
    

    int exchange = a[num1];
    a[num1] = a[num2];
    a[num2] = exchange;
    }

    for (int i = 1; i <= n; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}