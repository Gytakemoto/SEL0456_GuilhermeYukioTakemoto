#include <stdio.h>

unsigned int fib(unsigned int n) {
if (n == 0 || n == 1)
    return 1;
  return fib(n - 1) + fib(n-2);
}

int main(){
unsigned int n;
int fibonacci;

printf("Entre com o valor de n: \n");
scanf("%d", &n);

fibonacci = fib(n);

printf("O valor do Fibonacci é: %d \n", fibonacci);
return 0;
}