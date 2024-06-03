from flask import Blueprint, render_template
import pathlib

this_path = pathlib.Path(__file__).parent.resolve().__str__()

home_blueprint = Blueprint('home', __name__, template_folder='templates_home', static_folder=this_path)

@home_blueprint.route("/")
def homepage():
    
    return render_template("home.html")