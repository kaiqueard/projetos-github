#include <stdio.h>

int main() {
    int N, M;
    if (scanf("%d %d", &N, &M) != 2) return 0;

    int max_turma[1005];
    for (int j = 0; j < M; j++) {
        max_turma[j] = 1;
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int votos;
            scanf("%d", &votos);
            if (votos > max_turma[j]) {
                max_turma[j] = votos;
            }
        }
    }

    int total = 0;
    for (int j = 0; j < M; j++) {
        total += max_turma[j];
    }

    printf("%d\n", total);
    
    return 0;
}