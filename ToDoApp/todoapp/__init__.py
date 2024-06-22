from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from todoapp.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    with app.app_context():
        db.create_all()

    bcrypt.init_app(app)

    from todoapp.main.routes import main
    from todoapp.users.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)
    
    return app