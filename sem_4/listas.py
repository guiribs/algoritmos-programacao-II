"""
Há basicamente 4 maneiras de se implementar
listas:
- Sequencial vs. Encadeada
- Estática vs. Dinâmica

Na alocação sequencial os elementos são
inseridos em sequência na memória, i.e.
sequência física.

Permite acesso aos elementos
por meio de índices.

Na alocação encadeada os elementos não estão
necessariamente em posições adjacentes de
memória, i.e. possuem uma sequência lógica.

Usa-se um ponteiro para
o primeiro elemento, e
cada elemento possui
um ponteiro para o
Próximo.

Quando utilizar sequencial ou encadeada?
- No caso da abordagem sequencial a vantagem
é poder acessar os elementos por meio dos
índices, porém a memória pode ser mal
utilizada.
- Na abordagem encadeada há otimização de
memória, mas perde-se o acesso direto aos
elementos intermediários da lista.
Obs. a linguagem Python implementa listas
usando a abordagem sequencial.

Estática vs. Dinâmica
Variação quanto ao tipo de alocação de
memória utilizado.
Na alocação estática toda memória é alocada
mesmo sem ser utilizada.
Na alocação dinâmica a memória é alocada sob
demanda, à medida que a lista cresce.

Quando utilizar alocação estática ou dinâmica?
- A alocação dinâmica permite gerenciar melhor
a memória, sendo útil quando não sabemos de
antemão quantos elementos iremos armazenar
na lista.
- A alocação estática é mais simples, pois a
alocação é feita apenas uma vez. Porém, pode
ser que a memória seja alocada mesmo sem
uso.
Obs. a linguagem Python implementa listas
usando a abordagem dinâmica.

Listas podem variar também em outros
aspectos:
- Ordenada vs. não ordenada  (sort() - funcao em Python para ordernar uma lista)
- Linear vs. não linear
- Homogênea vs. heterogênea
"""
lista = []
