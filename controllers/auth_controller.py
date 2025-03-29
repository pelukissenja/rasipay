from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from models.user import db, User
from forms import RegistrationForm, LoginForm

def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = User.hash_password(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Akun berhasil dibuat! Silakan login.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)

def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Login berhasil!", "success")
            return redirect(url_for("dashboard.dashboard"))
        flash("Login gagal! Periksa email dan password.", "danger")

    return render_template("login.html", form=form)

def logout():
    logout_user()
    flash("Anda telah logout.", "info")
    return redirect(url_for("home"))
