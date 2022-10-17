########################################################################################################################
#Aluno: Guilherme Yukio Takemoto
#Nusp: 11800796
########################################################################################################################


f = open("separador.txt", "r")

print(f.read())

f.close()

f = open("separador.txt", "r")                                          #Abrindo o arquivo

new_line_list = list()                                                  #Definindo listas para linhas e textos modificados
new_text_list = list()


for line in f:                                                          #Iterando através das linhas
    #print("->", line)
    word = line.split()                                                 #Separando as palavras
    if '"' in line:                                                     #Analisa se há " na linha
        #print(word)
        for i in range(len(word)):      
            if '"' not in word[i]:      
                new_word = word[i].replace(",",";")                     #Se não houver " na palavra, simplesmente substitui "," por ";"
            else:
                word_letters = list(word[i])                            #Cria uma lista das letras de cada palavra
                if word_letters[-1] == ",":                             #Se o último caracter da palavra for ",", substitui por ";"
                    word_letters[-1] = ";"
                new_word = ''.join(str(term) for term in word_letters)  #Transformando a nova palavra em string  
            new_line_list.append(new_word)                              #Adicionando string em uma nova lista
        new_line_list.append("\n")                                   
        new_line = ' '.join(str(term) for term in new_line_list)        #Transformando a nova linha em string
        new_line_list = []                                              #Limpando a lista para as próximas linhas
    else:
        new_line = line.replace(",",";")                                #Caso não haja " , apenas substitui , por ;
    new_text_list.append(new_line)                                      #Armazena linha no novo arquivo .txt
    #print(new_line, "\n")

new_text = ''.join(str(term) for term in new_text_list)                #Transforma o texto em uma string

f.close()

f = open("novo_separador.txt", "w+")                                    #Salvando novo arquivo
f.write(new_text)
f.close

print("\n")
f = open("novo_separador.txt", "r")
print(f.read())



            


