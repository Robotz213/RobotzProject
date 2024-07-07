# Função para formatar como moeda brasileira
import babel.numbers as numbers
from babel.dates import format_date

def format_currency_brl(value):
    return numbers.format_currency(value, 'BRL', locale='pt_BR')

# Função para formatar a data e obter o nome do mês em português
def format_date_brl(date):
    return format_date(date, format='MMMM', locale='pt_BR').capitalize()