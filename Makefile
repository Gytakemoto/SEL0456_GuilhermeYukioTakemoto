GCC = gcc

Fibonacci: Fibonacci.c fib.c
	$(GCC) $^ -g -lm -o $@
