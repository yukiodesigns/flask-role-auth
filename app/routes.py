from flask import render_template, Blueprint
from .auth.views import auth
from flask_login import current_user, login_required
# Create a main Blueprint
main = Blueprint('main', __name__)

# Register the authentication Blueprint
main.register_blueprint(auth)

@main.route('/dashboard')
@login_required  # Ensure user is logged in
def dashboard():
    # Get the current logged-in user
    user = current_user

    # Pass 'user' variable to the template
    return render_template('dashboard.html', user=user)