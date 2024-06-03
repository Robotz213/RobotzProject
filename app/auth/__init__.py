from flask import Blueprint, render_template, redirect, url_for
import pathlib

this_path = pathlib.Path(__file__).parent.resolve().__str__()

auth_blueprint = Blueprint('auth', __name__, template_folder = 'templates_auth', static_folder = this_path)

@auth_blueprint.route("/login")
def login():
    
    return render_template("login.html")

@auth_blueprint.route("/logout")
def logout():
    
    # flash("Sessão encerrada!", "success")
    return redirect( url_for("auth.login") )