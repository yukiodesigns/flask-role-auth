from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, current_user
from .forms import LoginForm, RegistrationForm
from app.models import User
from app import db 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))  # Redirect to dashboard if user is already logged in

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):  # Assuming you have a method like check_password to verify the password
            login_user(user)  # Log in the user

            if user.role == 'admin':
                return redirect(url_for('main.admin_dashboard'))
            else:
                return redirect(url_for('main.dashboard'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger')

    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        role = form.role.data 
        
        if role not in ['user', 'admin']:
            flash('Invalid role selected. Please try again.', 'danger')
            return redirect(url_for('auth.register'))

        # Create a new user instance
        new_user = User(username=username, role=role)  # Assuming role_id 1 is for regular users
        new_user.set_password(password)  # Set the password using set_password method

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('main.auth.login'))

    return render_template('register.html', form=form)