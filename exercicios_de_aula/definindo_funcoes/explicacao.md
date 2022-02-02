# Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;

- Podem ou não recber entradas de dados e retornar uma saída de dados;

- Muito úteis para executar procedimentos similarespor repetidas vezes;

- Se você escrever uma função que realiza várias tarefas dentro dela, é interessante 
fazer uma verificação para que a função seja simplificada;

- Toda função integrada do Python é chamada de built-in;

- O nome da função deve ser sempre em letras minúsculas e em caso de nome composto, 
separados por underline(Snake Case);

- Parâmetros são opconais e podem ou não ser separados por vírgula;

- O bloco de função, também chamado de corpo da função ou implementação, é onde 
o processamento da função ocorre, podendo ou não ter retorno;

- Para definirmos uma função, utilizamos a palavra reservada **def** e o bloco de código é aberto com os **:**;

- A função é chamada ao se colocar o nome dela fora dela mesma (em caso de não recursividade). EX: 
```
def diz_oi():
    print('oi')
    print()
diz_oi() 
```
- Return finaliza a função;

- Podemos ter em uma função diferentes returns;

- Podemos em uma função, retornar qualquer tipo de dado e multiplos valores;

- Funções com parâmetros, recebem dados para serem processads dentro dela mesma;

- Funções que possuem parâmetro padrão, tem sua passagem de parâmetro opcional
como por exemplo a função **print()**

- Funções com parâmetro padrão são mais flexíveis, evitam erros com parâmetros incorretos e 
deixa o código mais legível;