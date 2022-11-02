#Nome: Guilherme Yukio Takemoto 
#NUSP: 11801049
#----------------------------------------------------------------------------------------------------------------------

fib = lambda x: fib(x-1) + fib(x-2) if x>=2 else 1
fact = lambda z: z * fact(z-1) if z>=2 else 1


with open("funcional.txt") as original: num = original.read()

list_fib = [] 
list_fact = []

for k in range(len(num)) :
    if num[k] == ',' or num[k] == ' ' :       
        list_fib.append(num[k-1])
        list_fact.append(num[k+1])

with open("novo_funcional.txt",'w') as novo:
    for k in range(len(list_fib)) :
        novo_arq = list(map(lambda k, x, z: f"Linha {k+1} : Fib = {fib(int(x))} Fact = {fact(int(z))} \n", range(len(list_fib)), list_fib, list_fact))
    print(novo_arq)
    novo.write(''.join(str(term) for term in novo_arq))
        