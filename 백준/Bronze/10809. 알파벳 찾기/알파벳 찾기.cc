#include <stdio.h>

int main(void)
{
    char word[101];
    int positions[26];
    int i;

    scanf("%s", word);

    for (i = 0; i < 26; i++) {
        positions[i] = -1;
    }

    for(i = 0; word[i] != '\0'; i++)
    {
        int index = word[i] - 'a';
        if(positions[index] == -1)
            positions[index] = i;
    }

    for(i = 0; i < 26; i++)
    {
        printf("%d ", positions[i]);
    }

    return 0;
}