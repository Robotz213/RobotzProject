# Seu módulo principal onde o Blueprint é registrado
from flask import Blueprint, render_template
from app.models.sql.mysql.law.processos import Processos
from app.utils import format_currency_brl
import pathlib

this_path = pathlib.Path(__file__).parent.resolve().__str__()

dashboard_blueprint = Blueprint(
    'dashboard', __name__, template_folder='templates_dashboard')


@dashboard_blueprint.route("/")
def dashboard():

    database = Processos.query.all()

    total_proc = 0
    condenado = 0
    
    for item in database:
        total_proc = total_proc + item.valor_causa

    for item in database:
        condenado = condenado - float(item.valor_causa)
    
    total_proc = format_currency_brl(total_proc)
    condenado = format_currency_brl(condenado)

    pagina = "pages/dashboard.html"
    return render_template("index.html", pagina=pagina,
                           database=database, format_currency_brl=format_currency_brl,
                           total_proc = total_proc, condenado = condenado)
