#include <stdio.h>
#include "fib.h"

int main(){
unsigned int n;
int fibonacci;

printf("Entre com o valor de n: \n");
scanf("%d", &n);

fibonacci = fib(n);

printf("O valor do Fibonacci eh: %d \n", fibonacci);
return 0;
}