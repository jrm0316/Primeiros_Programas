"""
Crie um PACOTE chamado utilidadesCeV que tenha dois MÓDULOS INTERNOS chamados MOEDA e DADO.
Transfira todas as funções utilizadas nos DESAFIOS 107, 108 e 109 para o primeiro pacote e
mantenha tudo funcionando.
"""
from exercicio112.utilidadescev import Moeda
from exercicio112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$')
Moeda.resumo(p, 20, 12)
