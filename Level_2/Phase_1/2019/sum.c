#include <stdio.h>

int main(void) {
  int square, number_sum, rectangle = 0;
  /*square are number of square, number_sum is number of sum that 
  we want and rectangle are number of rectangles that the sum equals the sum variable*/

  scanf("%i %i", &square, &number_sum);

  
  int values[square];
  //values are values of sequence

  for(int i = 0; i <= square - 1; i++){
    scanf("%i", &values[i]);
    //add values
    
  }

  int sum = 0;
  //sum is sum of values into from loop

  for(int i = 0; i <= square - 1; i++){
    sum += values[i];
    if(sum == number_sum){
      ++rectangle;
    } else if(sum > number_sum) {
      sum = values[i];
      sum = (sum > number_sum) ? 0 : values[i];
    }

  }
  printf("%i", rectangle);
  return 0;
}
