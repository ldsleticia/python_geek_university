# Módulo Random

 - São arquivos em Python

 - Deixam o código simples e com eles é possível reutilização de códigos

 - Podem ser compartilhados pela comunidade

 - O módulo random possui várias funções para geração de números aleatórios

 - Existem duas formas de se utilizar um módulo ou função do random():

Da forma abaixo, você importa todo o módulo random() 

 ~~~
import random
 ~~~

É uma forma pouco recomendada caso você saiba quais funções quer importar do módulo random()

- Utilizando o ***dir(random)*** é possível visualizar quais funções existem dentro desse método

- Ao utilizar uma função do pacote randon(), você precisa fazer a separação por ponto entre uma e outra

 ~~~
print(random.random())
 ~~~

 - Não confunda a função random com o pacote random. A função random() termina com parênteses e faz parte do pacote random

 - Realizando o import de apenas uma função do random

  ~~~
from random import random
 ~~~