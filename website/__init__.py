from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dbName = "database.db"
app = Flask(__name__)
db = SQLAlchemy(app)

def create_app():

    app.config['SECRET_KEY'] = 'QWERTYUIOP'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbName}'

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Note

    with app.app_context():
        db.create_all()

    return app