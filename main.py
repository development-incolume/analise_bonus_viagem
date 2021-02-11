#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
from pathlib import Path
import pandas as pd
from twilio.rest import Client
import toml

config = Path('conf/config.toml').resolve()


def send_sms(destinatario, msg=None, remetente=None):
    remetente = remetente or '+12674940492'
    msg = msg or "Hello from Python!"
    # Your Account SID from twilio.com/console
    account_sid = toml.load(config)['twilio']['account_sid']
    # Your Auth Token from twilio.com/console
    auth_token = toml.load(config)['twilio']['auth_token']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=destinatario,
        from_=remetente,
        body=msg
    )
    print(message.sid)


# Abrir os arquivo xlsx
fxlsx = Path('dados').glob('*.xlsx')
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tb_vendas = pd.read_excel(f'dados/{mes}.xlsx')
    cond = tb_vendas.VENDAS > 55000
    if cond.any():
        # print(tb_vendas)
        # print(tb_vendas.loc[cond])
        vendedor = tb_vendas.loc[cond, 'VENDEDOR'].values[0]
        vendas = tb_vendas.loc[cond, 'VENDAS'].values[0]
        # print(vendedor)
        # print(vendas)
        msg = f'Em {mes}, a meta > 55k, foi atingida por "{vendedor} com R$ {vendas:.2f}"'
        print(msg)
        send_sms('+5561999092244', msg)

    # Para cada arquivo:
    #     Verificar se algum valor na coluna vendas é superior a 55k
    #     se for maior que 55k -> envia SMS o Nome, Mês e as vendas do vendedor

