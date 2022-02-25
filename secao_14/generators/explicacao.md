# Generators

- Geradores ou generators, são iterables mas o contrário não é verdadeiro

- Generators podem ser criados com funções geradoras
  - Funções geradoras recebem a palavra reservada yield;
  - Generators podem ser criados com expressões geradoras;
  
- Ao usar o next() a primeira passagem já foi iterada e caso você use novamente, começará do índice [1];

- Diferenças entre funções e generators functions
  - ***Funções***:
    - Utilizam return
    - Retorna somente uma vez
    - Quando executada retorna um valor
  - ***Generator Function***
    - Utilizam yield
    - Podem utilizar yield múltiplas vezes
    - Quando executada, retorna um generator
    - Não é um generator, ela gera um generator