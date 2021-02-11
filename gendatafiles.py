#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import pandas as pd
from faker import Faker
import locale
import random
import toml
from pathlib import Path

dados = Path('dados/dados.toml')
dados.parent.mkdir(exist_ok=True)
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
fake = Faker('pt_BR')


def gen_names():
    """ Gera os 1000 nomes aleatórios utilizando a biblioteca Faker """
    # Semente para garantir que sempre serão os mesmos nomes
    fake.seed_instance(0)
    # dict com os 1000 nomes completos
    names = {'VENDEDOR': (f"{fake.first_name()} {fake.last_name()}" for x in range(1000))}
    # grava o resultado em um arquivo toml para recuperação posterior
    with open('dados/dados.toml', 'w') as f:
        toml.dump(names, f)


def gendata():
    """ Gera massa de dados com VENDEDOR/VENDAS """
    # Se não existir cria arquivo toml com nomes de entrada
    if not dados.is_file():
        gen_names()
    # Carrega nomes dos vendedores
    names = toml.load(dados)['VENDEDOR']
    # Semente aleatória para gerar valor de vendas diferentes
    fake.seed_instance(random.randint(1, 13))
    # gerador com 1000 entradas aleatórias para vendas
    vendas = (
        fake.pyfloat(left_digits=None, right_digits=2, positive=True, min_value=1000, max_value=55010)
        for _ in range(1000)
    )
    # Retorna uma lista de tuplas com VENDEDOR/VENDA
    return zip(names, vendas)


def run():
    """"""
    # Lista com nomes dos meses gerado em pandas
    meses = set(pd.date_range(start='2020-01-01', end='2020-6-1', periods=30).strftime('%B'))
    for mes in meses:
        # DataFrame com conjunto de dados gerados
        df = pd.DataFrame(gendata(), columns=['VENDEDOR', 'VENDAS'])
        # Grava arquivos com nomes dos meses em portugues com vendedores e suas respectivas vendas mensais
        df.to_excel(dados.with_name(f"{mes}.xlsx"), index=False)


if __name__ == '__main__':
    run()
