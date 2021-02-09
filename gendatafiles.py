#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import pandas as pd
from faker import Faker
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')


def gendata():
    fake = Faker('pt_BR')
    fake.seed_instance(0)
    names = (f"{fake.first_name()} {fake.last_name()}" for x in range(1000))
    vendas = (
        fake.pyfloat(left_digits=None, right_digits=2, positive=True, min_value=1000, max_value=55000)
        for _ in range(1000)
    )
    return zip(names, vendas)


def run():
    meses = set(pd.date_range(start='2020-01-01', end='2020-6-1', periods=30).strftime('%B'))
    df = pd.DataFrame(gendata(), columns=['VENDEDOR', 'VENDAS'])
    print(len(meses), meses)
    print(df)
    # for i in range(10):
    #     print(f"{fake.first_name()} {fake.last_name()}",
    #           fake.pyfloat(left_digits=None, right_digits=2, positive=True, min_value=10000, max_value=60000)
    #           )


if __name__ == '__main__':
    run()
