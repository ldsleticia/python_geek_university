# Classes

- Em POO são modelos dos objetos do mundo real sendo representados computacionalmente

Como exemplo, imagine que você deseja criar um sistema para automatizar o controle das
lâmpadas da sua casa:
   ~~~
      class Lampada:
       pass
    
      lamp = Lampada()
   ~~~ 
- Classes podem conter:
  - Atributos -> Representam as características do objeto. No caso da lâmpada,
  possivelmente iríamos querer saber sua voltagem, sua cor, sua luminosidade e etc;
  - Métodos (funções) -> Representam os comportamentos do objeto, as ações que ele
  pode realizar no seu sistema. No caso da lâmpada, um comportamento comum seria o
  de ligar e desligar a mesma;
  
- Utilizamos a palavra ***pass*** em Python quando ainda não temos um método 
implementado

- Quando nomeamos uma classe, utilizamos por convenção o nome com inicial em maiusculo
se o nome for comporto, as iniciais de ambas as palavras ficam em maiusculo e juntas
    ~~~    
    class ContaCorrente
        pass
    ~~~