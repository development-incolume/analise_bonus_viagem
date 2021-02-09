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
    fake.seed_instance(0)
    names = {'VENDEDOR': (f"{fake.first_name()} {fake.last_name()}" for x in range(1000))}
    with open('dados/dados.toml', 'w') as f:
        toml.dump(names, f)


def gendata():
    if not dados.is_file():
        gen_names()
    names = toml.load(dados)['VENDEDOR']
    fake.seed_instance(random.randint(1, 13))
    vendas = (
        fake.pyfloat(left_digits=None, right_digits=2, positive=True, min_value=1000, max_value=55000)
        for _ in range(1000)
    )
    return zip(names, vendas)


def run():
    meses = set(pd.date_range(start='2020-01-01', end='2020-6-1', periods=30).strftime('%B'))
    # print(list(gendata()))
    df = pd.DataFrame(gendata(), columns=['VENDEDOR', 'VENDAS'])
    print(len(meses), meses)
    print(df)
    print(random.randint(1, 13))
    # for i in range(10):
    #     print(f"{fake.first_name()} {fake.last_name()}",
    #           fake.pyfloat(left_digits=None, right_digits=2, positive=True, min_value=10000, max_value=60000)
    #           )


if __name__ == '__main__':
    run()
