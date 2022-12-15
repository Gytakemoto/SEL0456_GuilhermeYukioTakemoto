Repositório para disciplina SEL0456

Aluno: Guilherme Yukio Takemoto
NUSP: 11800796

<h1 align="center"> Trabalho Final </h1>

<p align="justify"> O trabalho final pode ser encontrado na pasta Trabalho Final deste repositório.

<p align="justify"> O objetivo deste é desenvolver um conversor de unidades para diferentes grandezas, que possa ser atualizada pelo usuário. A interface gráfica foi desenvolvida pelo desenvolvedor de interface gráfica Glade, e pode ser vista na Figura 1:

<p align="center"> Figura 1: Interface gráfica desenvolvida.
<p align="center"> <img src="https://user-images.githubusercontent.com/64660658/207889193-c5b4d9d6-78c7-4f4e-a746-cee68f587e53.png">

<p align="justify">Para adicionar novas grandezas e unidades no arquivo, basta editar a planilha trabalho_final.xls. Esta está organizada de uma maneira específica, de forma que sua edição deve ser feita da forma exposta na Figura 2:

<p align="center"> Figura 2: Configuração da planilha.
<p align="center"> <img src="https://user-images.githubusercontent.com/64660658/207887078-07611d4e-dd94-429a-bba7-3bb29e6faa34.png">

<p align="justify"> Nas colunas ímpares (A,C,E,...) estão armazenadas a grandeza (1ª linha) e as unidades relacionadas à mesma. Note que a primeira unidade (2ª linha) deve ser a que será tomada como referência para as demais (no caso na planilha default, adotou-se as unidades do S.I como referência). Nas colunas pares (B,D,F,...), deve-se adicionar o fator de multiplicação de cada unidade em relação à unidade de referência colocada, por exemplo, para o kg, deve-se colocar 1000, pois 1kg = 1000g.

<p align="justify"> A fim de carregar os dados modificados da planilha para interface gráfica, deve-se apertar o botão "Carregar dados da planilha". Certifique-se de salvar o arquivo ".xls" antes de fazer isso. 


