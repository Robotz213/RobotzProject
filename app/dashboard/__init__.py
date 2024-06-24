from flask import Blueprint, render_template, redirect, flash, url_for
import pathlib

from clear import clear

this_path = pathlib.Path(__file__).parent.resolve().__str__()

dashboard_blueprint = Blueprint('dashboard', __name__, template_folder = 'templates_dashboard')

@dashboard_blueprint.route("/")
def dashboard():
    
    pagina = "pages/dashboard.html"
    return render_template("index.html", pagina = pagina)


