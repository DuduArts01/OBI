#include <iostream>

using namespace std;

int main(void){
    int N, I, P, posB;
    
    cin >> N;
    cin >> I;
    cin >> P;
    
    if(I + P <= N){
        posB = I + P;
    } else{
        posB = (I + P) % N;
    }
    
    cout << posB;

    return 0;
}