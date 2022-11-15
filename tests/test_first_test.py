f = open("test.txt", "r")

def fact(x):
    if x >= 2:
        return x * fact(x-1)
    else:
        return 1

def fib(x):
    if x > 2:
        return fib(x-1) + fib(x-2)
    else:
        return 1


def test_answer():
  
  list_fibo = list()
  list_fact = list()

  for line in f:
      #print(line.split())
      if line.split():  #Se line.split() for vazio "[]", então line.plit = FALSE e pula a linha
        number = line.split() #Coletando os números das linhas
        try:
          assert fact(int(number[0])) == int(number[1]) #Checa se o Fatorial bate
        except:
          print("Cálculo do Fatorial falhou! " + str(fact(int(number[0]))) + " != " + number[1])
          assert False
        try:
          assert fib(int(number[0])) == int(number[2]) #Checa se o Fibonacci bate
        except:
          print("Cálculo do Fibonacci falhou! " + str(fib(int(number[0]))) + " != " + number[2])
          assert False


test_answer()


