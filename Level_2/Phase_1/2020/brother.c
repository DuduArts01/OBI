#include <stdio.h>
int main(int argc, char *argv[])
{
	int N;
	//N would be the age of Otávio's younger brother
	scanf("%i", &N);
	
	int M;
	//M would be age of Otavio
	scanf("%i", &M);
	
	int L;
	//L would be the age of Otavio's older brother
	
	int reason = M - N;
	//find the reason for the arithmetic progression
	L = M + reason;
	//add Otavio's age with the ratio to find his older brother's age
	
	printf("%i", L);
	
	
}