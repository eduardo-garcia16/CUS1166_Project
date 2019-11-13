from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_manage import ManagingCourse

def create_app(config_class = Config):
  app = Flask(__name__)
  app.config.from_object(Config)
  db = SQLAlchemy(app)
  migrate = Migrate(app, db)
  manage = ManagingCourse(app)


from app import routes, models
