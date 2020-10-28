from app import app

@app.route('/')
def index():
    return "Python is awesome!"

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"