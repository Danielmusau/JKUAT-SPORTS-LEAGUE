from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from JSL.config import Config

app = Flask(__name__)
app.config.from_object(Config)
    
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)
    
from JSL.users.routes import users
from JSL.teams.routes import teams
from JSL.main.routes import main
from JSL.errors.handlers import errors
        
app.register_blueprint(users)
app.register_blueprint(teams)
app.register_blueprint(main)
app.register_blueprint(errors)
