#include <stdio.h>

int main(void) {
    int M, N, P;

    scanf("%i", &M);
    scanf("%i", &N);

    int R[M][N];
    for(int l = 0; l < M; ++l){
        for(int c = 0; c < N; ++c){
            scanf("%i", &R[l][c]);
        }
    }

    scanf("%i", &P);

    int i, j, sold = 0;

    for(int x = 0; x < P; ++x){
        scanf("%i", &i);
        scanf("%i", &j);

        if(R[i - 1][j - 1] > 0) {
            ++sold;
            R[i - 1][j - 1] -= 1;
        }
        
    }
    
    printf("%i", sold);
    return 0;
}   