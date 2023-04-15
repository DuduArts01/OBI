#include <stdio.h>

int main(void){
    char games[12] = {};
    int V = 0;
    int group = 0;
    
    for(int i = 0; i < 12; ++i){
        scanf("%c", &games[i]);
        if ( games[i] == 'V' || games[i] == 'v' ) {
            ++V;
        }
    }
    if(V >= 5){
        group = 1;
    } else if ( V >= 3 ) {
        group = 2;
    } else if ( V >= 1 ) {
        group = 3;
    } else {
        group = -1;
    }
    printf("%i\n", group);
    return 0;
}


