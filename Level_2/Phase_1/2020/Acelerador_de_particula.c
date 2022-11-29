#include <stdio.h>

int main() {
    int D, rest, sensor;
    scanf("%i", &D);
    
    D -= 3;
    //Discounts 3 km
    
    if(D <= 8) {
        //When D  < 8
        if(D == 3){
            sensor = 1;
        } else if(D == 4) {
            sensor = 2;
        } else {
            sensor = 3;
        }
        
    } else{
        while(D < 8){
            rest = D % 8;
            D = D / 8;
            //complete one loop
            
        }
    }
if(rest == 3){
        sensor = 1;
    } else if(rest == 4) {
        sensor = 2;   
    } else {
        sensor = 3;
    }

    
   
  
    return 0;
}
