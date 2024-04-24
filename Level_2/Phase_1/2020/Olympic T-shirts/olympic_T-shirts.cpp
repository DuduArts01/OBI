#include <iostream>

using namespace std;

int main(void)
{
    int N, T, P, M;
    int p = 0;
    int m = 0;
    
    cin >> N;
    
    for(int i = 0; i < N; i++){
        cin >> T;
        T == 1? p++ : m++; 
    }
    
    cin >> P;
    cin >> M;  
    
    cout << ((p == P) and (m == M) ? "S" : "N");
    

    return 0;
}
