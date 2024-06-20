from flask import Flask

def create_app():
    app = Flask(__name__)

    from todoapp.main.routes import main

    app.register_blueprint(main)
    
    return app