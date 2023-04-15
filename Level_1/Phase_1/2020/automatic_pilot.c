#include <stdio.h>
int verification (int A, int B, int C);
int main(void)
{
    int Amain, Bmain, Cmain, result;
    scanf("%d %d %d", &Amain, &Bmain, &Cmain);
    verification(Amain, Bmain, Cmain);
    result = verification(Amain, Bmain, Cmain);
    printf("%d\n", result);
    return 0;
}

int verification(int A, int B, int C){
    int car;
    if((B-A) < (C-B)){
        car = 1;
    } else if ((B-A) > (C-B)){
        car = -1;
    } else{
        car = 0;
    }

    return car;
}

