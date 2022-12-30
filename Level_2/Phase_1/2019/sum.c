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

  //loop to count how many sum rectangles are in the sequence
  for(int i = 0; i <= square - 1; i++){    
    sum += values[i];
    //sum values    
    if(sum == number_sum){
      ++rectangle;
      //verify sum and if the sum equals the desired sum, add 1 to the rectangular sum variable
    } else if(sum > number_sum) {
      sum = values[i];
      //if the sum is greater than the desired sum, we add the value of the sequence number where it stopped
      if(sum == number_sum) {
        ++rectangle;
        //if the sum equals the desired sum, add 1 to the rectangular sum variable
      }

    }

  }
  printf("%i", rectangle);
  ///show the final result
  
  return 0;
}
