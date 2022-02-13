# Leitura de arquivos

- Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada ***open()*** que literalmente significa abrir.

- A forma mais simples de utilização do ***open()*** nós passamos apenas um parâmetro e entrada, que nesse caso é o nome do arquivo a ser lido.
Essa função retorna um _io.TextIOWrapper e é com ele que trabalhos.

- Quando abrimos um arquivo com a função ***open()*** é criada uma conexão entre o arquivo no disco do computador e o programa e essa conexão se
chama streaming; para encerrar essa conexão, precisamos utilizar a função ***close()***.

- ***closed()*** retorna True quando o arquivo está fechado e False se o arquivo estiver aberto

- A função ***open()*** abre o arquivo para a leitura, ou seja, esse arquivo precisa existir. Caso contrário, teremos o erro ***FileNotFoundError***.

- mode r significa modo de leitura.

- Para ler o conteúdo de um arquivo após sua abertura, devemos utilizar a função ***read()***.

- É possível limitar a quantidade de itens que o ***read()*** irá ler

- Ao utilizar a função ***read()***, o Python lê nosso arquivo inteiro como uma grande string e em alguns casos é interessante que a leitura
seja feita linha a linha. Para tal, utilizamos a função ***readline()***.

- Com o ***readline()*** é possível usar a função ***split()*** e transformar a string em uma lista.

- ***redlines()*** transforma cada linha em uma lista

- Utilizamos ***seek()*** para movimentar o cursor dentro do texto.

- Se tentarmos manipular um arquivo após seu fechamento, teremos o retorno de ***ValueError***