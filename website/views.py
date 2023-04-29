from flask import Blueprint, render_template

# Don't need to share the name with the file, but helps with consistency
views = Blueprint('views', __name__)

# Define page with a decorator
@views.route('/')
def home():
    return render_template("home.html")