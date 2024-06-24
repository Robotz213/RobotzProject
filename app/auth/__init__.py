from flask import Blueprint, render_template, redirect, url_for, flash
from app.auth.form.auth_form import LoginForm

import pathlib

this_path = pathlib.Path(__file__).parent.resolve().__str__()

auth_blueprint = Blueprint('auth', __name__, template_folder = 'templates_auth', static_folder = this_path)

@auth_blueprint.route("/login", methods = ["GET", "POST"])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        
        flash("Logado com sucesso!", "success")
        return redirect(url_for('dashboard.dashboard'))
    
    return render_template("login.html", form = form)

@auth_blueprint.route("/logout")
def logout():
    
    # flash("Sessão encerrada!", "success")
    return redirect( url_for("auth.login") )