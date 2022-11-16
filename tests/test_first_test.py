f = open("tests/test.txt", "r")

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
  
  erros = list()
  messages = list()

  for line in f:
      #print(line.split())
      if line.split():  #Se line.split() for vazio "[]", então line.plit = FALSE e pula a linha
        number = line.split() #Coletando os números das linhas
        try:
          assert fact(int(number[0])) == int(number[1]) #Checa se o Fatorial bate
        except:
          erros.append(line)
          messages.append("Cálculo do Fatorial falhou! " + str(fact(int(number[0]))) + " != " + number[1])
          #assert False
        try:
          assert fib(int(number[0])) == int(number[2]) #Checa se o Fibonacci bate
        except:
          erros.append(line)
          messages.append("Cálculo do Fibonacci falhou! " + str(fib(int(number[0]))) + " != " + number[2])
          #assert False
    
  print(messages)

  if erros != []:
    print(f"Foram encontrados {len(erros)} erro(s):")
    for n in range(len(erros)):
      print(messages[n])
    assert False


test_answer()


