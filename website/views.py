from flask import Blueprint

# Don't need to share the name with the file, but helps with consistency
views = Blueprint('views', __name__)

# Define page with a decorator
@views.route('/')
def home():
    return "<h1>Test</h1>"