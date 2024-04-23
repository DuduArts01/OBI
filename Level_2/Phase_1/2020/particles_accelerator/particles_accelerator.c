#include <stdio.h>

int main(void){
  int N;
  scanf("%i", &N);
  printf((N - 6) % 8 + 1);
  
  return 0;
}
