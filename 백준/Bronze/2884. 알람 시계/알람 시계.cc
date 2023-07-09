#include <stdio.h>

int main(void)
{
    int hour, minute;
    scanf("%d %d", &hour, &minute);

    int tempMinute = hour * 60 + minute;
    tempMinute = (tempMinute < 45) ? (tempMinute + 24 * 60 - 45) : (tempMinute - 45);

    hour = tempMinute / 60;
    minute = tempMinute % 60;

    printf("%d %d", hour, minute);

    return 0;
}
