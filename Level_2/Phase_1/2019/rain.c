#include <stdio.h>

//Shelves will be represented by "#"
//wall will be represented by "."
//a leak point represented by the character "o"

int verification();

int main()
{
    int N, M;
    //N is line and M is column
    
    scanf("%i", &N);
    scanf("%i", &M);
    
    char C[N][M], Cf[N][M];
    //C is matrice of rain and limit is 500 for line and column
    
    for(int l = 0; l < N; ++l){
        for(int c = 0; c < M; ++c){
            scanf("%c", &C[l][c]);
        }
    }
    
    Cf = verification(C[l][c])
    
    
    

    return 0;
}

