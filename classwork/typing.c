#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int i;
    char list[] = "Hello World";
    size_t length = strlen(list);

    for (i = 0; i < length; i++)
    {
        printf("%c", list[i]);
        
    }
    printf("\n");
    printf("%d", i);
    printf("\n");
    return(0);
}