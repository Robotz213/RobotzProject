# Seu módulo principal onde o Blueprint é registrado
from flask import Blueprint, render_template, jsonify
from app.models.sql.mysql.law.processos import Processos
from app.utils import format_currency_brl, format_date_brl
import pathlib
import pandas as pd

from collections import Counter
this_path = pathlib.Path(__file__).parent.resolve().__str__()

dashboard_blueprint = Blueprint(
    'dashboard', __name__, template_folder='templates_dashboard')


@dashboard_blueprint.route("/")
def dashboard():

    database = Processos.query.all()

    total_claimed = 0
    judgment_amount = 0
    
    for item in database:
        total_claimed += float(item.valor_causa)

    for item in database:
        judgment_amount -= float(item.valor_causa)
    
    total_claimed = format_currency_brl(total_claimed)
    judgment_amount = format_currency_brl(judgment_amount)

    page = "pages/dashboard.html"
    return render_template("index.html", page = page,
        database=database, format_currency_brl=format_currency_brl, total_claimed = total_claimed, judgment_amount = judgment_amount)
    
@dashboard_blueprint.route("/grafico_processos")
def graficoproc():
    
    processos = Processos.query.all()
    data = [{
        'distribuition_date': processo.distribuicao_data,
        'value_claim': processo.valor_causa
    } for processo in processos]
    
    df = pd.DataFrame(data)
    df['distribuition_date'] = pd.to_datetime(df['distribuition_date'])
    df['year_month'] = df['distribuition_date'].dt.to_period('M')
    df['month_name'] = df['distribuition_date'].apply(format_date_brl)
    result = df.groupby('month_name')['value_claim'].sum().reset_index()
    
    result['month_name'] = pd.Categorical(result['month_name'])
    result = result.sort_values('month_name')
    
    data = {
        "month_name": result['month_name'].to_list(),
        "value_claim": result['value_claim'].to_list(),
        "max_claimed ":  df['value_claim'].max()
    }
    
    return jsonify(data)
