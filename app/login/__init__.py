from flask import Blueprint, render_template
import pathlib
import os

this_path = pathlib.Path(__file__).parent.resolve().__str__()

templates_path = os.path.join(this_path, "templates")

dashboard_blueprint = Blueprint('dashboard', __name__, template_folder=templates_path, static_folder="static_dashboard")

@dashboard_blueprint.route("/")
def dashboard():
    
    return render_template("index.html")