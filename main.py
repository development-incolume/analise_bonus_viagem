#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from pathlib import Path
import pandas as pd


# Abrir os arquivo xlsx
fxlsx = Path('dados').glob('*.xlsx')
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    print(mes)
    tb_vendas = pd.read_excel(f'dados/{mes}.xlsx')
    print(tb_vendas)
    if (tb_vendas.VENDAS > 55000).any():
        print(f'Em {mes}, a meta > 55k, foi atingida')

    # Para cada arquivo:
    #     Verificar se algum valor na coluna vendas é superior a 55k
    #     se for maior que 55k -> envia SMS o Nome, Mês e as vendas do vendedor

