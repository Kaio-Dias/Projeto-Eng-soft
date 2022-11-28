
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # secret key de dev
    app.secret_key = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
    db.init_app(app)
    
    #from .models import Usuario
    #with app.app_context(): 
    #    db.create_all()
    
    # blueprint de autenticacao
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app