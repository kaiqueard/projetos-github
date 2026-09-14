#include <stdio.h>

int main(void)
{
    int T, D, M;
    int i, y, anterior, folga, maior;

    if (scanf("%d %d %d", &T, &D, &M) != 3)
    {
        return 1;
    }

    anterior = 0;
    maior = 0;
    for (i = 0; i < M; i++)
    {
        if (scanf("%d", &y) != 1)
        {
            return 1;
        }
        folga = y - anterior;
        if (folga > maior)
        {
            maior = folga;
        }
        anterior = y;
    }

    folga = D - anterior;
    if (folga > maior)
    {
        maior = folga;
    }

    printf("%c\n", maior >= T ? 'Y' : 'N');

    return 0;
}