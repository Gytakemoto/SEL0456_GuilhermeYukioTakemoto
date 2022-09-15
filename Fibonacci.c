#include <stdio.h>

int main(){
int n, i, aux1, aux2, fib;
n = 1;
aux1 = 0;
aux2 = 1;
fib = 0;

printf("Entre com o valor de n: \n");
scanf("%d", &n);


if (n == 0 || n == 1)
    fib = n;
else{
    for(i = 2; i <= n; i++){
        fib = aux1 + aux2;
        aux1 = aux2;
        aux2 = fib;
    }
}

printf("O valor do Fibonacci é: %d \n", fib);
return 0;
}