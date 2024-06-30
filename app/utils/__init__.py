# Função para formatar como moeda brasileira
import babel.numbers as numbers

def format_currency_brl(value):
    return numbers.format_currency(value, 'BRL', locale='pt_BR')