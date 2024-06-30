# Seu módulo principal onde o Blueprint é registrado
from flask import Blueprint, render_template
from app.models.sql.mysql.law.processos import Processos
from app.utils import format_currency_brl 
import pathlib

this_path = pathlib.Path(__file__).parent.resolve().__str__()

dashboard_blueprint = Blueprint('dashboard', __name__, template_folder='templates_dashboard')

@dashboard_blueprint.route("/")
def dashboard():
    database = Processos.query.all()
    pagina = "pages/dashboard.html"
    return render_template("index.html", pagina=pagina, database=database, format_currency_brl = format_currency_brl)


